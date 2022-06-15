class gui():
    def __init__(self):

        buttons_distance = settings.width/16
        self.settings_button = image_button(
            settings.width/100, settings.height - settings.height/9,
            image = 'buttons/gui/settings.png',
            image_selected = 'buttons/gui/settings_active.png',
            scale = (settings.height/150)/1.5
        )

        self.play_fast_button = image_button(
            settings.width/100 + buttons_distance, settings.height - settings.height/9,
            image = 'buttons/gui/play_fast.png',
            image_selected = 'buttons/gui/play_fast_active.png',
            scale = (settings.height/150)/1.5
        )

        self.play_button = image_button(
            settings.width/100 + (buttons_distance)*2, settings.height - settings.height/9,
            image = 'buttons/gui/play.png',
            image_selected = 'buttons/gui/play_active.png',
            scale = (settings.height/150)/1.5
        )

        self.pause_button = image_button(
            settings.width/100 + (buttons_distance)*3, settings.height - settings.height/9,
            image = 'buttons/gui/pause.png',
            image_selected = 'buttons/gui/pause_active.png',
            scale = (settings.height/150)/1.5
        )

    def on_mouse_motion(self, x, y, dx, dy):
        self.settings_button.on_mouse_motion(x, y, dx, dy)
        self.play_fast_button.on_mouse_motion(x, y, dx, dy)
        self.play_button.on_mouse_motion(x, y, dx, dy)
        self.pause_button.on_mouse_motion(x, y, dx, dy)

    def on_mouse_press(self, x, y, dx, dy):
        self.settings_button.on_mouse_press(x, y, dx, dy)
        self.play_fast_button.on_mouse_press(x, y, dx, dy)
        self.play_button.on_mouse_press(x, y, dx, dy)
        self.pause_button.on_mouse_press(x, y, dx, dy)

    def draw(self):
        if get_obj_other('setings_game').draw_gui and not get_obj_display('world').menu:
            drawp(self.settings_button)
            drawp(self.play_fast_button)
            drawp(self.play_button)
            drawp(self.pause_button)
