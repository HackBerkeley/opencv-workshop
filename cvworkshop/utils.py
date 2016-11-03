from sys import platform

if platform in ["linux", "linux2"]:
    # linux
    pass
elif platform in ["darwin"]:
    # OS X
    pass
elif platform in ["win32", "cygwin", "win"]:
    # Windows...
    pass
