## 2026-04-22 - Keyboard shortcut clarity in the Ink shell
**Learning:** Keyboard guidance in a terminal app becomes noisy when every pane advertises the same shortcuts and visually ambiguous when unfocused panes keep accent styling.
**Action:** Keep shortcut hints context-aware to the active pane, render inline keys in a distinct bold treatment, and dim inactive panes so keyboard focus is unambiguous.
## 2024-03-24 - Consistent Keyboard Shortcut Styling & Contextual Prompt Hints
**Learning:** Terminal UI users depend heavily on visual consistency for keyboard navigation cues. We found that pagination shortcuts (`[ ]`) were rendered as plain text in the workspace component, missing the application's established pattern (`<Text color="white" bold>`) for keybindings, which reduced discoverability. Furthermore, static action hints like "Enter to run" create confusing states when an action is actively running (`busy=true`) and input is temporarily disabled.
**Action:** Always wrap inline keyboard shortcut references in a consistent highlight pattern (`<Text color="white" bold>` against `gray` helper text) by updating string-based layout rows to support rendering arbitrary `ReactNode`s when necessary. Additionally, conditionally render interactive hints (like "Enter to run") so they only appear when the action is actually available to the user.

## 2024-04-26 - [Interactive Pane State Hierarchy and Input Swallowing]
**Learning:** Terminal interfaces with multiple interactive panes (like actions, history, output, and input) must explicitly scope single-character keyboard shortcuts to their intended active pane to prevent swallowing input intended for text inputs. Furthermore, users often lose context of which pane is active without clear visual hierarchy.
**Action:** Always scope single-character shortcuts (e.g. `[`, `]`, `d`) to specific focus states (e.g., `focusPane === "output"`, `focusPane !== "input"`). Dim the text color of header titles for inactive panes (e.g., to `gray`) to create a clear visual hierarchy and direct attention to the active workspace.

## 2024-05-18 - Visual Hierarchy & Box Boundary Alignment
**Learning:** Terminal UI applications can suffer from visually ambiguous focus states when nested panes rely only on header text color while the bounding Box remains a static color. Users failed to distinguish which pane in a split layout was currently receiving input commands.
**Action:** Always align the text color of the active pane's header with the `borderColor` of its enclosing `<Box>`. Ensure interactive components like the Workspace, LeftRail, and RightRail dynamically switch border colors (e.g., to `cyanBright` or `magentaBright`) when their specific pane receives focus, rather than retaining a static fallback color.
