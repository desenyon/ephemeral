<div align="center">

<img src="./assets/ephemeral-logo.svg" alt="Ephemeral Research Desk" width="920">

# Ephemeral

### A terminal-native research desk for markets, models, and decision loops.

[![Version](https://img.shields.io/badge/version-4.1.0-ff9f0a?style=for-the-badge&logo=python&logoColor=white)](./ephemeral/version.py)
[![Interface](https://img.shields.io/badge/interface-Ink%206%20Research%20Desk-0a0a0a?style=for-the-badge)](https://github.com/vadimdemedes/ink)
[![Python](https://img.shields.io/badge/python-3.11+-111827?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Node](https://img.shields.io/badge/node-required-12f7a6?style=for-the-badge&logo=nodedotjs&logoColor=0a0a0a)](https://nodejs.org/)

Ephemeral turns a terminal into a professional research workstation: live symbol context, watchlists, news, backtests, model routing, setup health, artifacts, and a command dock that never gets out of the way.

</div>

---

## The Desk

```text
 EPHEMERAL RESEARCH DESK SPY v4.1.0                        LIVE · ready
 Research / Ask / Research · Ask · local ready              workspace ready
 ┌────────────────────┐ ┌────────────────────────────────────┐ ┌────────────────────┐
 │ WATCHLIST          │ │ ASK                     workspace  │ │ CONTEXT            │
 │ > SPY   621.40 +0.2│ │ Thesis, catalysts, risk, compare   │ │ SPY $621.40 +0.2%  │
 │   QQQ   548.90 +0.4│ │                                    │ │ SETUP              │
 │   DIA   443.10 -0.1│ │ /quote AAPL                        │ │ No blockers        │
 │                    │ │ /news NVDA                         │ │ NEWS               │
 │ RESEARCH           │ │ /compare AAPL MSFT                 │ │ Headlines loaded   │
 │ > Ask              │ │ /backtest AAPL -s sma_crossover    │ │ ARTIFACTS          │
 │   Quote            │ │                                    │ │ Reports, charts    │
 └────────────────────┘ └────────────────────────────────────┘ └────────────────────┘
 ┌───────────────────────────────────────────────────────────────────────────────────┐
 │ Ask                                                            READY · Enter to run│
 │ > What changed in NVDA's thesis after the latest guide?                           │
 └───────────────────────────────────────────────────────────────────────────────────┘
```

This is not a launcher. It is a shell for staying inside one research loop:

| Surface | What it does |
| :--- | :--- |
| Market chrome | Shows the active symbol, routing state, readiness, and current workflow. |
| Watchlist rail | Keeps indexes, active tickers, and workflows visible while you work. |
| Workspace | Renders the selected result, raw payloads, research output, or command response. |
| Context rail | Shows quote state, setup issues, related news, artifacts, and warnings. |
| Command dock | Runs natural-language requests and slash commands from anywhere. |

---

## Why It Exists

Most finance tools split attention across dashboards, notebooks, terminals, browser tabs, and chat windows. Ephemeral compresses that into one keyboard-first environment:

- Ask for thesis work, catalysts, and risk checks.
- Pull quotes, headlines, comparisons, charts, and backtests.
- Route through local or cloud LLM providers — OpenAI, Anthropic, Google, Groq, xAI, NIM, or Ollama — with BYOK keys stored in your OS keychain.
- Race the same question across the native router, the [Pi](https://pi.dev) coding-agent harness, and OpenAI Codex CLI, side by side.
- Describe a trading strategy in English and get it written, backtested, and charted in one turn.
- Keep provider setup, local-model state, and dependency health visible.
- Export charts, reports, and session artifacts under `~/.ephemeral/`.

The result is fast enough for terminal work and structured enough for real research.

---

## Install

```bash
curl -fsSL https://raw.githubusercontent.com/desenyon/ephemeral/main/scripts/install.sh | bash
```

Pin a release:

```bash
curl -fsSL https://raw.githubusercontent.com/desenyon/ephemeral/main/scripts/install.sh | EPHEMERAL_REF=v4.1.0 bash
```

Requirements:

| Requirement | Why |
| :--- | :--- |
| Python `3.11+` | CLI, bridge, data services, model routing |
| Node.js + `npm` | Ink Research Desk frontend |
| `curl` + `tar` | One-line installer |

Launch:

```bash
ephemeral
```

If `~/.local/bin` is not on your `PATH`, run `~/.local/bin/ephemeral` directly or add that directory to your shell profile.

---

## Source Setup

```bash
git clone https://github.com/desenyon/ephemeral.git
cd ephemeral
uv sync --extra dev
npm install --prefix ephemeral/ink_ui
uv run ephemeral
```

Classic virtualenv flow:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
npm install --prefix ephemeral/ink_ui
pip install -e ".[dev]"
ephemeral
```

---

## Command Map

### Research Desk

| Command | Result |
| :--- | :--- |
| `ephemeral` | Launch the default Ink Research Desk. |
| `ephemeral --legacy-ui` | Launch the legacy Textual interface. |
| `ephemeral --ink-ui` | Force Ink and fail instead of falling back. |

### One-shot workflows

| Command | Result |
| :--- | :--- |
| `ephemeral ask "What changed in AAPL's thesis?"` | Run a tool-aware LLM request. |
| `ephemeral strategize "Momentum rotation into QQQ above its 50d average"` | Describe a strategy in English; the model writes, backtests, and charts it. |
| `ephemeral quote AAPL MSFT NVDA` | Fetch quote snapshots. |
| `ephemeral news NVDA -n 12` | Produce a headline digest. |
| `ephemeral compare META GOOGL AMZN` | Compare returns, volatility, and quality metrics. |
| `ephemeral chart SPY --period 6mo` | Save a chart artifact. |
| `ephemeral backtest AAPL -s sma_crossover --period 2y` | Run the built-in backtest engine. |
| `ephemeral doctor` | Run dependency and environment checks. |
| `ephemeral tools` | List registered model tools. |

In the Research Desk, `/race` fires one question at the native provider, [Pi](https://pi.dev), and OpenAI Codex CLI simultaneously and shows all three answers side by side.

### Configuration

| Command | Result |
| :--- | :--- |
| `ephemeral --setup` | Run provider and local-model setup. |
| `ephemeral --status` | Show provider, model, key, and dependency health. |
| `ephemeral --list-models` | Print bundled model suggestions by provider. |
| `ephemeral --provider openai` | Persist a default provider. |
| `ephemeral --model gpt-5.4` | Persist a default model. |
| `ephemeral --setkey openai <key>` | Save an API key in `~/.ephemeral/config.env`. |

---

## Desk Shortcuts

| Key | Action |
| :--- | :--- |
| `Tab` | Cycle left rail, workspace, right rail, command dock. |
| `Left` / `Right` | Move between major panes when the dock is empty. |
| `Up` / `Down` or `j` / `k` | Move inside the focused pane or scroll output. |
| `/` | Start a slash command from any pane. |
| `[` / `]` | Page workspace output. |
| `d` | Toggle rendered/raw payload view. |
| `Esc` | Clear prompt and return focus to the command dock. |
| `Ctrl+C` | Quit. |

---

## Provider Setup

Cloud keys (BYOK — bring your own key):

```bash
ephemeral --setkey openai <your-key>
ephemeral --setkey anthropic <your-key>
ephemeral --setkey google <your-key>
ephemeral --setkey nim <your-key>
ephemeral --provider openai
ephemeral --model gpt-5.4
```

Keys are stored in your OS keychain (macOS Keychain / Windows Credential Manager / Linux Secret Service) when one is available, falling back to `~/.ephemeral/config.env` otherwise — never sent anywhere but the provider you configured.

NVIDIA NIM (`nim`) is an OpenAI-compatible endpoint with hosted OSS models (Llama, Mixtral, DeepSeek), including free-tier options — get a key at [build.nvidia.com](https://build.nvidia.com).

Local Ollama:

```bash
ollama serve
ollama pull qwen3.5:8b
ephemeral --provider ollama
ephemeral --model qwen3.5:8b
ephemeral --status
```

The Research Desk surfaces setup blockers in the context rail, so missing keys, unreachable Ollama, and unavailable local models are visible while you work.

### Alternate harnesses (optional)

`/race` and the Codex leg of any harness comparison need these installed separately — Ephemeral detects and reports each as unavailable rather than failing if you skip them:

```bash
npm i -g @earendil-works/pi-coding-agent   # Pi coding-agent harness
npm i -g @openai/codex                     # OpenAI Codex CLI
codex mcp add ephemeral -- <path-to-venv>/bin/python -m ephemeral.mcp_server
```

The `codex mcp add` step is a one-time, explicit registration of Ephemeral's tool server with Codex (writes to `~/.codex/config.toml`); Pi's project-local extension in `.pi/extensions/` is auto-discovered with no setup.

---

## Architecture

```mermaid
flowchart LR
  CLI["ephemeral CLI"] --> Ink["Ink Research Desk"]
  Ink --> Bridge["Persistent Python bridge"]
  Bridge --> Engine["Research engine"]
  Bridge --> Health["Setup and health"]
  Bridge --> Market["Market data services"]
  Bridge --> Tools["Tool registry"]
  Bridge --> Router["Native LLM router"]
  Bridge --> Pi["Pi harness agent"]
  Bridge --> Codex["Codex CLI agent"]
  Tools --> MCP["MCP server"]
  Pi --> MCP
  Codex --> MCP
  Engine --> Artifacts["Reports, charts, exports"]
  Market --> Cache["TTL cache under ~/.ephemeral"]
```

| Layer | Responsibility |
| :--- | :--- |
| `ephemeral/ink_ui` | React + Ink Research Desk frontend. |
| `ephemeral/ink_bridge.py` | Structured process boundary between Ink and Python workflows. |
| `ephemeral/research/workspace.py` | Failure-tolerant workspace snapshots for desk panels. |
| `ephemeral/cli.py` | CLI entry point and launcher orchestration. |
| `ephemeral/setup_agent.py` | Provider, key, and local-model onboarding. |
| `ephemeral/secure_store.py` | OS-keychain-backed BYOK secret storage, with plaintext fallback. |
| `ephemeral/llm` | Router and provider implementations (OpenAI, Anthropic, Google, Groq, xAI, NIM, Ollama). |
| `ephemeral/mcp_server.py` | Exposes the tool registry over MCP for external agent harnesses. |
| `ephemeral/agents` | Pi and Codex CLI harness backends. |
| `ephemeral/tools` | Model-callable research tools. |
| `ephemeral/backtest` | Built-in backtesting workflows plus the custom-strategy loader. |

---

## Quality Gates

```bash
uv run --extra dev pytest -q
npm --prefix ephemeral/ink_ui run typecheck
npm --prefix ephemeral/ink_ui run smoke
uv run ruff check .
```

Current Research Desk branch verification:

| Gate | Status |
| :--- | :--- |
| Python tests | `1010 passed, 1 deselected` |
| Ink typecheck | passing |
| Ink smoke render | passing |
| Ruff | passing |

---

## Build

```bash
./scripts/build.sh
```

Build outputs:

- Python distributions under `dist/`
- macOS app bundle through `scripts/create_app.py`

---

## Project State

- Release notes: [CHANGELOG.md](./CHANGELOG.md)
- Version source: [ephemeral/version.py](./ephemeral/version.py)
- License: [LICENSE](./LICENSE)

Ephemeral is built for people who want the terminal to feel like a desk, not a prompt.

<!-- architecture-atlas-v5:start -->
## Architecture Atlas v5

These editable Mermaid diagrams mirror the [Notion architecture dossier](https://app.notion.com/p/3b467342e8c1817dbf62ef0d9d793b93?pvs=204).

### 1. Research-desk anatomy

```mermaid
flowchart LR
  USER["Researcher / command dock"] --> SHELL["Ink terminal shell + screen/router state"]
  SHELL --> WATCH["Watchlist and preference manager"]
  SHELL --> MARKET["Quote and history adapters"]
  SHELL --> NEWS["News aggregation"]
  MARKET --> PACK["Research packet builder<br>values + provider + timestamp + provenance"]
  NEWS --> PACK
  PACK --> MODEL["Model router and provider adapters"]
  MODEL --> ANALYSIS["Hypotheses, risks, citations and explicit generated-analysis boundary"]
  PACK --> STRAT["Typed strategy schema"]
  STRAT --> SIGNAL["Signal engine"] --> PORT["Portfolio simulator"] --> COST["Cost/slippage model"] --> METRIC["Performance metrics"]
  ANALYSIS --> ART["Artifact repository"]
  METRIC --> CHART["Chart renderer"] --> ART
  ART --> MANIFEST[("Research packet, prompts, data hashes, run manifest, reports")]
  HEALTH["Setup health / doctor"] -. provider readiness .-> SHELL
```

### 2. Evidence-to-backtest wiring

```mermaid
flowchart TB
  CMD["symbol / compare / news / strategy / backtest command"] --> RESOLVE["Resolve providers and cache policy"] --> DATA["Fetch timestamped point-in-time market/news evidence"]
  DATA --> PROV["Attach provenance and staleness status"]
  PROV --> PACK["Freeze research packet"]
  PACK --> RESEARCH["Generate analysis with claims separated from evidence"]
  PACK --> SPEC["Compile typed strategy spec"]
  SPEC --> HIST["Validate historical data contract and window"] --> SIM["Signals -> positions -> costs -> portfolio path"] --> METRICS["Return, risk, drawdown, turnover and diagnostics"]
  RESEARCH --> REPORT["Research report with citations and risks"]
  METRICS --> REPORT
  REPORT --> SAVE["Persist charts, provider trace, assumptions, hashes and replay manifest"]
  OUTAGE["Provider outage"] --> FALLBACK["Fallback with preserved provenance or explicit offline degradation"] --> PACK
```

### 3. Runtime narrative

```mermaid
sequenceDiagram
  actor R as Researcher
  participant T as Terminal Shell
  participant D as Market / News Services
  participant M as Model Research Plane
  participant B as Backtest Engine
  participant A as Artifact Store
  R->>T: symbol, compare, news, strategy or backtest command
  T->>D: resolve providers, cache and freshness policy
  D-->>T: timestamped data and provenance
  T->>M: frozen research packet
  M-->>T: analysis, hypotheses, risks and citations
  opt strategy or backtest
    T->>B: typed strategy, data contract and assumptions
    B->>B: signals, positions, costs, metrics and diagnostics
    B->>A: run manifest, charts and data hashes
  end
  T->>A: report, prompts, provider trace and reproducibility status
  A-->>R: artifact links and replay instructions
```

### 4. Reliability model

```mermaid
stateDiagram-v2
  [*] --> HOME
  HOME --> SYMBOL_CONTEXT
  SYMBOL_CONTEXT --> RESEARCHING
  RESEARCHING --> GENERATING_STRATEGY
  GENERATING_STRATEGY --> BACKTESTING
  SYMBOL_CONTEXT --> COMPARING
  BACKTESTING --> EXPORTING
  RESEARCHING --> EXPORTING
  SYMBOL_CONTEXT --> OFFLINE_DEGRADED: provider unavailable
  RESEARCHING --> ERROR: ungrounded or malformed result
  BACKTESTING --> ERROR: invalid data contract or simulation
  ERROR --> HOME
  OFFLINE_DEGRADED --> HOME
```

<!-- architecture-atlas-v5:end -->
