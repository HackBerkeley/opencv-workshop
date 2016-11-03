import os
import cv2
import threading


def _module_exists(module_name):
    try:
        __import__(module_name)
    except ImportError:
        return False
    else:
        return True


def capture_screen(x1=0, y1=0, x2=0, y2=0, id=0, bw=False):
    w, h = x2-x1, y2-y1
    if w == 0 or h == 0:
        cmd = "screencapture screencaps/cap%d.jpg" % id
    else:
        cmd = "screencapture -R %d,%d,%d,%d screencaps/cap%d.jpg" % (x1, y1, w, h, id)
    os.system(cmd)
    if bw:
        return cv2.imread("screencaps/cap%d.jpg" % id, 0)
    else:
        return cv2.imread("screencaps/cap%d.jpg" % id)


osascript_characters = {
    ' ': 49,
    'left': 123,
    'right': 124,
    'up': 126,
    'down': 125
}


def press(char, length=None):
    key = osascript_characters[char] if char in osascript_characters else None
    assert char in osascript_characters, "Key for keystroke not in the key code dictionary. valid characters are" \
                                         "space: ' ' and the arrow keys: 'left', 'right', 'up', 'down'. " \
                                         "You can add more if you want (just look up Applescript Key Codes " \
                                         "and add them to the OSASCRIPT_CHARACTERS dictionary in utils_mac.py)"

    cmd = """osascript -e 'tell application "System Events"' """
    if length is not None:
        cmd += """-e 'key down (key code %d)' -e 'delay %f' -e 'key up (key code %d)' """ % (key, length, key)
    else:
        cmd += """-e 'key code %d' """ % (key)
    cmd += """-e 'end tell'"""
    os.system(cmd)


def hit_space():
    cmds = ["""osascript -e""",
            """'tell application "System Events"'""",
            """-e 'set activeApp to name of first application process whose frontmost is true'""",
            """-e 'if not (("Terminal" is in activeApp) or ("Python" is in activeApp)) then'""",
            """-e 'keystroke " "'""",
            """-e 'end if'""",
            """-e 'end tell'"""]
    cmd = " ".join(cmds)
    thread = threading.Thread(target=os.system, args=(cmd,))
    thread.start()


def get_img_path(id=0):
    return "screencaps/cap%d.jpg" % id

if _module_exists("pyautogui"):
    import pyautogui as pa
    pa.FAILSAFE = True
    press = pa.press
    mouse_position = pa.position

else:
    def position():
        raise ImportError("You must install pyautogui to use the position() function")

if "screencaps" not in os.listdir("./"):
    os.system("mkdir screencaps")
