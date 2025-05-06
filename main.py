from pynput import keyboard
import keyboard as keyb
from pandas.io.clipboard import clipboard_get

def on_release(key, injected):
    # print(key)
    if key == keyboard.Key.esc:
        # Stop listener
        # keyb.write(clipboard_get())
        return False
    if key == keyboard.Key.space:
       #keyboard.press(keyboard.Key.backspace)
        keyb.write(clipboard_get())

def on_press(key, injected):
    pass


with keyboard.Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()

