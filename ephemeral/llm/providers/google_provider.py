import asyncio
import logging
from typing import Any, AsyncIterator, Callable, Dict, List, Optional, Union

from .base import BaseLLM

logger = logging.getLogger(__name__)

class GoogleProvider(BaseLLM):
    """Google Gemini client."""

    provider_name = "google"

    def __init__(self, api_key: str, rate_limiter=None):
        super().__init__(rate_limiter)
        # Assuming google-genai is installed as per pyproject.toml
        from google import genai
        self.client = genai.Client(api_key=api_key)

    async def generate(
        self,
        messages: List[Dict[str, str]],
        model: str,
        tools: Optional[List[Dict[str, Any]]] = None,
        on_tool_call: Optional[Callable] = None,
        stream: bool = True,
        json_mode: bool = False,
    ) -> Union[str, AsyncIterator[str]]:
        await self._wait_for_rate_limit()

        from google.genai import types

        system_prompt = None
        contents = []

        for msg in messages:
            role = msg["role"]
            content = msg["content"]

            if role == "system":
                system_prompt = content
            elif role == "user":
                contents.append(types.Content(
                    role="user",
                    parts=[types.Part(text=content)]
                ))
            elif role == "assistant":
                # Handle prior function calls structure if present?
                # For simplicity, assuming text for now, or simple tool handling
                contents.append(types.Content(
                    role="model",
                    parts=[types.Part(text=content)] if content else []
                ))

        config = types.GenerateContentConfig(
            system_instruction=system_prompt,
        )

        if tools:
            function_declarations = []
            for tool in tools:
                if tool.get("type") == "function":
                    func = tool["function"]
                    function_declarations.append(types.FunctionDeclaration(
                        name=func["name"],
                        description=func.get("description", ""),
                        parameters=func.get("parameters", {}),
                    ))
            if function_declarations:
                config.tools = [types.Tool(function_declarations=function_declarations)]

        if stream:
            # Not implementing stream for Google fully with tool loop yet implicitly
            # But will do basic check
             return self._stream_response(model, contents, config, on_tool_call, tools, messages)
        else:
             return await self._block_response(model, contents, config, on_tool_call, tools, messages)

    async def _block_response(self, model, contents, config, on_tool_call, tools, messages):
        from google.genai import types
        response = self.client.models.generate_content(
            model=model,
            contents=contents,
            config=config,
        )

        if response.candidates:
            candidate = response.candidates[0]
            if candidate.content and candidate.content.parts:
                function_calls = []
                text_response = ""
                for part in candidate.content.parts:
                    if part.text:
                        text_response += part.text
                    if part.function_call:
                        function_calls.append(part.function_call)

                if function_calls and on_tool_call:
                    contents.append(candidate.content)

                    function_responses = []
                    for fc in function_calls:
                        args = dict(fc.args) if fc.args else {}
                        try:
                            result = await on_tool_call(fc.name, args)
                        except Exception as e:
                            result = {"error": str(e)}

                        function_responses.append(types.Part(
                            function_response=types.FunctionResponse(
                                name=fc.name,
                                response={"result": str(result)} # Google expects dict
                            )
                        ))

                    contents.append(types.Content(role="user", parts=function_responses))

                    return await self._block_response(model, contents, config, on_tool_call, tools, messages + [{"role": "tool_exec", "content": "executed"}])

                return text_response
        return ""

    async def _stream_response(self, model, contents, config, on_tool_call, tools, messages) -> AsyncIterator[str]:
        """Stream tokens without blocking the asyncio event loop (sync SDK iterator)."""

        def _open_stream(self_ref: "GoogleProvider"):
            return self_ref.client.models.generate_content_stream(
                model=model,
                contents=contents,
                config=config,
            )

        response_stream = await asyncio.to_thread(_open_stream, self)

        def _next_chunk(it):
            try:
                return next(it)
            except StopIteration:
                return None

        stream_iter = iter(response_stream)
        accumulated_text = ""
        function_calls = []

        while True:
            chunk = await asyncio.to_thread(_next_chunk, stream_iter)
            if chunk is None:
                break
            if chunk.text:
                accumulated_text += chunk.text
                yield chunk.text

            if chunk.candidates and chunk.candidates[0].content and chunk.candidates[0].content.parts:
                for part in chunk.candidates[0].content.parts:
                    if part.function_call:
                        function_calls.append(part.function_call)

        if function_calls and on_tool_call:
             # Handle tool loop similar to block response
             # We need to reconstruct the content to append to history
            from google.genai import types

            assistant_content_parts = []
            if accumulated_text:
                assistant_content_parts.append(types.Part(text=accumulated_text))
            for fc in function_calls:
                assistant_content_parts.append(types.Part(function_call=fc))

            contents.append(types.Content(role="model", parts=assistant_content_parts))

            function_responses = []
            for fc in function_calls:
                args = dict(fc.args)
                try:
                    result = await on_tool_call(fc.name, args)
                except Exception as e:
                    result = str(e)
                function_responses.append(types.Part(function_response=types.FunctionResponse(name=fc.name, response={"result": str(result)})))

            contents.append(types.Content(role="user", parts=function_responses))

            # Recurse
            async for x in self._stream_response(model, contents, config, on_tool_call, tools, messages):
                yield x
