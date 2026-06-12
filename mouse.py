"""
mouse.py — Send fake mouse input using pynput
"""
import time
from pynput.mouse import Button, Controller

mouse = Controller()

def move(x: int, y: int):
    """Move mouse to absolute position."""
    mouse.position = (x, y)

def move_relative(dx: int, dy: int):
    """Move mouse by relative amount."""
    mouse.move(dx, dy)

def click(button: str = "left", count: int = 1):
    """Click a mouse button. button = 'left' | 'right' | 'middle'"""
    btn = {"left": Button.left, "right": Button.right, "middle": Button.middle}.get(button, Button.left)
    mouse.click(btn, count)

def scroll(dx: int = 0, dy: int = -3):
    """Scroll the mouse wheel. Negative dy = scroll down."""
    mouse.scroll(dx, dy)

def drag(x1: int, y1: int, x2: int, y2: int, duration: float = 0.5):
    """Click and drag from (x1,y1) to (x2,y2)."""
    mouse.position = (x1, y1)
    mouse.press(Button.left)
    steps = 20
    for i in range(steps + 1):
        t = i / steps
        mouse.position = (int(x1 + (x2 - x1) * t), int(y1 + (y2 - y1) * t))
        time.sleep(duration / steps)
    mouse.release(Button.left)

if __name__ == "__main__":
    time.sleep(2)
    move(500, 500)
    click("left")
    scroll(0, -3)
