# USB HID Device Emulator

Emulate keyboard, mouse, and gamepad input from Python. Includes a web UI and macro system.

## Structure
```
emulator/       → keyboard.py, mouse.py, gamepad.py
macros/         → JSON macro files
ui/             → Web dashboard (open in browser)
main.py         → Flask REST API server
```

## Quick Start

```bash
pip install -r requirements.txt
python main.py
```

Open http://localhost:5001

## Run a macro directly

```bash
# 2-second delay so you can switch to target window
python emulator/macro_runner.py macros/gaming.json
```

## Write your own macro (JSON)

```json
{
  "name": "My macro",
  "commands": [
    { "action": "hotkey", "keys": ["ctrl", "s"] },
    { "action": "wait",   "seconds": 0.2 },
    { "action": "type",   "text": "Hello!" }
  ]
}
```

### Supported actions
| Action   | Parameters |
|----------|-----------|
| `key`    | `key` — key name e.g. `"enter"`, `"f5"` |
| `hotkey` | `keys` — list e.g. `["ctrl","c"]` |
| `type`   | `text`, optional `delay` |
| `click`  | `button` (left/right/middle), `count` |
| `move`   | `x`, `y` |
| `scroll` | `dx`, `dy` |
| `wait`   | `seconds` |

## Notes
- Gamepad emulation requires **Windows** + ViGEmBus driver
- On Linux use `xdotool` as an alternative
- Always add a `wait` at the start so you can switch windows

## License
MIT
