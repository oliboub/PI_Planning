import os
import PySimpleGUI as sg
from screeninfo import get_monitors

### set display in center of standard screen

class MyWindow(sg.Window):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def get_default_screen_dimensions(self):
        default_monitor = [monitor for monitor in get_monitors() if monitor.is_primary][0]
        screen_width, screen_height = default_monitor.width, default_monitor.height
        return screen_width, screen_height

    def my_move_to_center(self):
        if not self._is_window_created('tried Window.move_to_center'):
            return
        screen_width, screen_height = self.get_default_screen_dimensions()
        win_width, win_height = self.size
        x, y = (screen_width - win_width)//2, (screen_height - win_height)//2
        self.move(x, y)

print(os.getcwd(),__name__,'imported')
