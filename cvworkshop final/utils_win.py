import os
import win32com.client


def _module_exists(module_name):
    try:
        __import__(module_name)
    except ImportError:
        return False
    else:
        return True


def get_key(char):
    keys = {
        ' ': ' ',
        'left': '{LEFT}',
        'right': '{RIGHT}',
        'up': '{UP}',
        'down': '{DOWN}'
    }
    char = char.lower()
    return keys[char] if char in keys else None


def press(char, length=None):
    key = get_key(char)
    key = key if key is not None else char

    shell = win32com.client.Dispatch("WScript.Shell")
    shell.SendKeys(key)


def get_img_path(id=0):
    return "screencaps/cap%d.jpg" % id


if _module_exists("pyscreenshot"):
    import pyscreenshot as ImageGrab

    def capture_screen(x1=0, y1=0, x2=0, y2=0, id=0):
        img = ImageGrab.grab(bbox=(x1, y1, x2, y2))
        img.save("screencaps/cap%d.jpg" % id)
else:
    raise ImportError("Please install pyscreenshot with 'pip install pyscreenshot'")


newpath = r'screencaps'
if not os.path.exists(newpath):
    os.makedirs(newpath)
