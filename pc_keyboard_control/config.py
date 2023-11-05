from screeninfo import get_monitors

def get_screen_resolution():
    for monitor in get_monitors():
        return monitor.width, monitor.height;
