"""
keyboard.py — Send fake keyboard input using pynput
"""
import time
from pynput.keyboard import Key, Controller

keyboard = Controller()

SPECIAL_KEYS = {
    "enter":     Key.enter,
    "space":     Key.space,
    "backspace": Key.backspace,
    "tab":       Key.tab,
    "esc":       Key.esc,
    "shift":     Key.shift,
    "ctrl":      Key.ctrl,
    "alt":       Key.alt,
    "up":        Key.up,
    "down":      Key.down,
    "left":      Key.left,
    "right":     Key.right,
    "f1": Key.f1, "f2": Key.f2, "f3": Key.f3, "f4": Key.f4,
    "f5": Key.f5, "f6": Key.f6, "f7": Key.f7, "f8": Key.f8,
    "f9": Key.f9, "f10": Key.f10, "f11": Key.f11, "f12": Key.f12,
}

def press_key(key: str):
    """Press and release a single key (e.g. 'a', 'enter', 'f5')."""
    k = SPECIAL_KEYS.get(key.lower(), key)
    keyboard.press(k)
    keyboard.release(k)

def type_text(text: str, delay: float = 0.05):
    """Type a string character by character."""
    for ch in text:
        keyboard.press(ch)
        keyboard.release(ch)
        time.sleep(delay)

def hotkey(*keys: str):
    """Press a combination of keys (e.g. 'ctrl', 'c')."""
    resolved = [SPECIAL_KEYS.get(k.lower(), k) for k in keys]
    for k in resolved:
        keyboard.press(k)
    for k in reversed(resolved):
        keyboard.release(k)

if __name__ == "__main__":
    time.sleep(2)
    type_text("Hello from USB HID Emulator!")
    press_key("enter")
