import keyboard
from pandas.io.clipboard import clipboard_get
if __name__ == "__main__":
    while True:
        #print("copy the text you would to write, then press 5. When ready to paste, press 6")
        content = clipboard_get()
        #keyboard.wait("e")
        print("press 6 to write whenever ready")
        keyboard.wait("1")
        #keyboard.write(content)
