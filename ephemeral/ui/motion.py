"""Shared motion constants for the TUI (loaders, tool rows, status)."""

# Braille (primary)
SPINNER_BRAILE: tuple[str, ...] = ("⠋", "⠙", "⠹", "⠸", "⠼", "⠴", "⠦", "⠧", "⠇", "⠏")

# Unicode arc (secondary layer / alternation)
SPINNER_ARC: tuple[str, ...] = ("◜", "◠", "◝", "◞", "◡", "◟")

# Dense “orbit” ring
SPINNER_RING: tuple[str, ...] = ("⎛", "⎜", "⎝", "⎞", "⎟", "⎠")

def combined_loader_frame(frame_index: int) -> str:
    """Blend two motion layers for a richer busy indicator."""
    a = SPINNER_BRAILE[frame_index % len(SPINNER_BRAILE)]
    b = SPINNER_ARC[(frame_index // 2) % len(SPINNER_ARC)]
    return f"{a}{b}"
