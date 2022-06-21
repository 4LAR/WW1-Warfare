class pause_gui():
    def __init__(self):

        buttons_distance = settings.height/6.5
        font_scale = 10;

        self.background = label(0, 0, settings.width, settings.height, (0, 0, 0), alpha=128)

        self.continue_button = image_button(
            settings.width/40, settings.height - settings.height/1.8,
            image = 'buttons/big/button.png',
            image_selected = 'buttons/big/button_active.png',
            scale = settings.height/150,
            text='continue',
            function=get_obj_display('game_rule')._unpause_settings,
            text_color=BUTTONS_FONT_COLOR,
            text_indent=settings.width/40,
            text_scale=BUTTONS_FONT_SCALE,
            text_size_y=1.3
        )

        self.restart_button = image_button(
            settings.width/40, settings.height - settings.height/1.8 - buttons_distance,
            image = 'buttons/big/button.png',
            image_selected = 'buttons/big/button_active.png',
            scale = settings.height/150,
            text='restart',
            arg='play(\'%s\')' % get_obj_display('world_save').name,
            text_color=BUTTONS_FONT_COLOR,
            text_indent=settings.width/40,
            text_scale=BUTTONS_FONT_SCALE,
            text_size_y=1.3
        )

        self.exit_button = image_button(
            settings.width/40, settings.height - settings.height/1.8 - (buttons_distance)*2.5,
            image = 'buttons/big/button.png',
            image_selected = 'buttons/big/button_active.png',
            scale = settings.height/150,
            text='exit',
            function=menu,
            text_color=BUTTONS_FONT_COLOR,
            text_indent=settings.width/40,
            text_scale=BUTTONS_FONT_SCALE,
            text_size_y=1.3
        )

    def on_mouse_motion(self, x, y, dx, dy):
        if get_obj_display('game_rule').pause_settings:
            self.continue_button.on_mouse_motion(x, y, dx, dy)
            self.restart_button.on_mouse_motion(x, y, dx, dy)
            self.exit_button.on_mouse_motion(x, y, dx, dy)

    def on_mouse_press(self, x, y, dx, dy):
        if get_obj_display('game_rule').pause_settings:
            if self.continue_button.on_mouse_press(x, y, dx, dy): return True
            if self.restart_button.on_mouse_press(x, y, dx, dy): return True
            if self.exit_button.on_mouse_press(x, y, dx, dy): return True

    def draw(self):
        if get_obj_display('game_rule').pause_settings:
            self.background.draw()
            self.continue_button.draw()
            self.restart_button.draw()
            self.exit_button.draw()
