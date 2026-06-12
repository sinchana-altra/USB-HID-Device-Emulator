"""
macro_runner.py — Load and execute macros from JSON files
"""
import json
import time
from pathlib import Path
from keyboard import press_key, type_text, hotkey
from mouse import click, move, scroll

def run_macro(commands: list, verbose: bool = True):
    for cmd in commands:
        action = cmd.get("action", "")
        if verbose:
            print(f"  [macro] {action}: {cmd}")

        if action == "type":
            type_text(cmd["text"], delay=cmd.get("delay", 0.05))

        elif action == "key":
            press_key(cmd["key"])

        elif action == "hotkey":
            hotkey(*cmd["keys"])

        elif action == "click":
            click(cmd.get("button", "left"), cmd.get("count", 1))

        elif action == "move":
            move(cmd["x"], cmd["y"])

        elif action == "scroll":
            scroll(cmd.get("dx", 0), cmd.get("dy", -3))

        elif action == "wait":
            time.sleep(cmd.get("seconds", 0.5))

        else:
            print(f"  Unknown action: {action}")

def load_and_run(json_path: str):
    path = Path(json_path)
    if not path.exists():
        print(f"Macro file not found: {json_path}")
        return
    with open(path) as f:
        data = json.load(f)
    print(f"Running macro: {data.get('name', path.stem)}")
    run_macro(data.get("commands", []))

if __name__ == "__main__":
    import sys
    if len(sys.argv) < 2:
        print("Usage: python macro_runner.py macros/example.json")
    else:
        time.sleep(2)
        load_and_run(sys.argv[1])
