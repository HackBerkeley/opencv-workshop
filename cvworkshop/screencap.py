from gi.repository import Gdk
from sys import argv

_, x1, y1, w, h = argv

x1, y1, w, h = list(map(int, [x1, y1, w, h]))

rootwindow = Gdk.get_default_root_window()
screenWidth, screenHeight = rootwindow.get_geometry()[2:4]

if x1 == y1 == h == w == 0:
    screenshot = Gdk.pixbuf_get_from_window(rootwindow, 0, 0, screenWidth, screenHeight)
else:
    screenshot = Gdk.pixbuf_get_from_window(rootwindow, x1, y1, w, h)
    name = "screencaps/cap0.png"
    screenshot.savev(name, "png", (), ())

