class gui():
    def __init__(self):

        buttons_distance = settings.width/16

#----------------------------TOP-HOTBAR-----------------------------------------

        self.settings_button = image_button(
            settings.width/100, settings.height - settings.height/9,
            image = 'buttons/gui/settings.png',
            image_selected = 'buttons/gui/settings_active.png',
            scale = (settings.height/150)/1.5,

            arg='get_obj_display(\'game_rule\')._pause_settings()'
        )

        self.play_fast_button = image_button(
            settings.width/100 + buttons_distance, settings.height - settings.height/9,
            image = 'buttons/gui/play_fast.png',
            image_selected = 'buttons/gui/play_fast_active.png',
            scale = (settings.height/150)/1.5,

            arg='get_obj_display(\'game_rule\')._play_fast()'
        )

        self.play_button = image_button(
            settings.width/100 + (buttons_distance)*2, settings.height - settings.height/9,
            image = 'buttons/gui/play.png',
            image_selected = 'buttons/gui/play_active.png',
            scale = (settings.height/150)/1.5,

            arg='get_obj_display(\'game_rule\')._play()'
        )

        self.pause_button = image_button(
            settings.width/100 + (buttons_distance)*3, settings.height - settings.height/9,
            image = 'buttons/gui/pause.png',
            image_selected = 'buttons/gui/pause_active.png',
            scale = (settings.height/150)/1.5,

            arg='get_obj_display(\'game_rule\')._pause()'
        )
#-----------------------------INFO-LABEL----------------------------------------

        self.pause_text = text_label(
            settings.width/2, settings.height - settings.height/8,
            'pause',
            size=settings.height//10,
            anchor_x='center',
            load_font=True,
            font='urod.ttf',
            color = BUTTONS_FONT_COLOR
        )

        self.pause_anim_delay = 0.8
        self.pause_anim_time = time.perf_counter() + self.pause_anim_delay
        self.pause_anim_flag = False

#-----------------------------DOWN-HOTBAR---------------------------------------

        

#-------------------------------------------------------------------------------

    def update(self):
        if get_obj_display('game_rule').pause and not get_obj_display('game_rule').pause_settings:
            if self.pause_anim_time <= time.perf_counter():
                self.pause_anim_flag = not self.pause_anim_flag

                self.pause_anim_time = time.perf_counter() + self.pause_anim_delay

    def on_mouse_motion(self, x, y, dx, dy):
        if get_obj_other('setings_game').draw_gui and not get_obj_display('world').menu and not get_obj_display('game_rule').pause_settings:
            self.settings_button.on_mouse_motion(x, y, dx, dy)
            self.play_fast_button.on_mouse_motion(x, y, dx, dy)
            self.play_button.on_mouse_motion(x, y, dx, dy)
            self.pause_button.on_mouse_motion(x, y, dx, dy)

    def on_mouse_press(self, x, y, dx, dy):
        if get_obj_other('setings_game').draw_gui and not get_obj_display('world').menu and not get_obj_display('game_rule').pause_settings:
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

            if get_obj_display('game_rule').pause and self.pause_anim_flag and not get_obj_display('game_rule').pause_settings:
                self.pause_text.draw()
