import os
import cv2

threading = False

def _module_exists(module_name):
    try:
        __import__(module_name)
    except ImportError:
        return False
    else:
        return True


if _module_exists("gi"):
    from gi.repository import Gdk

    rootwindow = Gdk.get_default_root_window()
    screenWidth, screenHeight = rootwindow.get_geometry()[2:4]

    def capture_screen(x1=0, y1=0, x2=0, y2=0):
        w, h = x2-x1, y2-y1
        os.system("python screencap.py %d %d %d %d" % (x1, y1, w, h))
        return cv2.imread("screencaps/cap0.png")

    def mouse_position():
        _, x, y, _ = rootwindow.get_pointer()
        return x, y

    def hit_space():
        ret = os.system("xdotool keydown space && sleep 0.1 && xdotool keyup space")
        if ret != 0:
            raise RuntimeError("xdotool not installed. run 'sudo apt-get install xdotool'")

    if threading:
        import threading
        def hit_space():
            cmd = "xdotool keydown space && sleep 0.1 && xdotool keyup space"
            thread = threading.Thread(target=os.system, args=(cmd,))
            thread.start()
else:
    raise ImportError("Please install Gtk+3")


if "screencaps" not in os.listdir("./"):
    os.system("mkdir screencaps")
