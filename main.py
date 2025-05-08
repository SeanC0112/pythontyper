from pynput import keyboard
import keyboard as keyb
from pandas.io.clipboard import clipboard_get
import time
def on_release(key, injected):
    # print(key)
    if key == keyboard.Key.esc:
        # Stop listener
        # keyb.write(clipboard_get())
        return False

def on_press(key, injected):
    if key == keyboard.Key.caps_lock:
        keyb.write(clipboard_get())
       #keyboard.press(keyboard.Key.backspace
        


with keyboard.Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()
