"""
gamepad.py — Simulate an Xbox 360 gamepad using vgamepad
Install: pip install vgamepad
Windows only (uses ViGEmBus driver)
"""
import time

try:
    import vgamepad as vg

    class Gamepad:
        def __init__(self):
            self.pad = vg.VX360Gamepad()

        def press_button(self, button: str):
            """Press and release a button. button = 'A','B','X','Y','LB','RB','START','SELECT'"""
            btn_map = {
                "A":      vg.XUSB_BUTTON.XUSB_GAMEPAD_A,
                "B":      vg.XUSB_BUTTON.XUSB_GAMEPAD_B,
                "X":      vg.XUSB_BUTTON.XUSB_GAMEPAD_X,
                "Y":      vg.XUSB_BUTTON.XUSB_GAMEPAD_Y,
                "LB":     vg.XUSB_BUTTON.XUSB_GAMEPAD_LEFT_SHOULDER,
                "RB":     vg.XUSB_BUTTON.XUSB_GAMEPAD_RIGHT_SHOULDER,
                "START":  vg.XUSB_BUTTON.XUSB_GAMEPAD_START,
                "SELECT": vg.XUSB_BUTTON.XUSB_GAMEPAD_BACK,
                "UP":     vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_UP,
                "DOWN":   vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_DOWN,
                "LEFT":   vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_LEFT,
                "RIGHT":  vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_RIGHT,
            }
            b = btn_map.get(button.upper())
            if b:
                self.pad.press_button(b)
                self.pad.update()
                time.sleep(0.05)
                self.pad.release_button(b)
                self.pad.update()

        def left_stick(self, x: float, y: float):
            """Set left stick. x, y in range -1.0 to 1.0"""
            self.pad.left_joystick_float(x_value_float=x, y_value_float=y)
            self.pad.update()

        def right_stick(self, x: float, y: float):
            self.pad.right_joystick_float(x_value_float=x, y_value_float=y)
            self.pad.update()

        def trigger(self, side: str, value: float):
            """Set trigger. side='left'|'right', value 0.0-1.0"""
            if side == "left":
                self.pad.left_trigger_float(value_float=value)
            else:
                self.pad.right_trigger_float(value_float=value)
            self.pad.update()

except ImportError:
    print("vgamepad not installed. Run: pip install vgamepad")
    class Gamepad:
        def press_button(self, b): print(f"[SIM] Button: {b}")
        def left_stick(self, x, y): print(f"[SIM] Left stick: ({x},{y})")
        def right_stick(self, x, y): print(f"[SIM] Right stick: ({x},{y})")
        def trigger(self, s, v): print(f"[SIM] Trigger {s}: {v}")

if __name__ == "__main__":
    g = Gamepad()
    g.press_button("A")
    g.left_stick(0.5, -0.5)
