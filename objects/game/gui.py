class gui():
    def __init__(self):

        buttons_distance = settings.width/16
        buttons_scale = (settings.height/150)/1.5

#----------------------------TOP-HOTBAR-----------------------------------------

        self.settings_button = image_button(
            settings.width/100, settings.height - settings.height/9,
            image = 'buttons/gui/settings.png',
            image_selected = 'buttons/gui/settings_active.png',
            scale = buttons_scale,

            arg='get_obj_display(\'game_rule\')._pause_settings()'
        )

        self.play_fast_button = image_button(
            settings.width/100 + buttons_distance, settings.height - settings.height/9,
            image = 'buttons/gui/play_fast.png',
            image_selected = 'buttons/gui/play_fast_active.png',
            scale = buttons_scale,

            arg='get_obj_display(\'game_rule\')._play_fast()'
        )

        self.play_button = image_button(
            settings.width/100 + (buttons_distance)*2, settings.height - settings.height/9,
            image = 'buttons/gui/play.png',
            image_selected = 'buttons/gui/play_active.png',
            scale = buttons_scale,

            arg='get_obj_display(\'game_rule\')._play()'
        )

        self.pause_button = image_button(
            settings.width/100 + (buttons_distance)*3, settings.height - settings.height/9,
            image = 'buttons/gui/pause.png',
            image_selected = 'buttons/gui/pause_active.png',
            scale = buttons_scale,

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

        self.units_buttons = []
        self.units_buttons_ico = []
        self.units_buttons_load = []
        self.units_buttons_time = []

        # world/units/ico/
        units_info = [
            ['human', 'get_obj_display(\'gui\').add_unit(0)'],
            ['human_with_mask', 'get_obj_display(\'gui\').add_unit(1)'],
            ['tank', 'get_obj_display(\'gui\').add_unit(2)'],
            ['tank', 'pass'],
            ['tank', 'pass']

        ]

        buttons_pos_y = settings.height/60

        for i in range(len(units_info)):
            self.units_buttons.append(
                image_button(
                    settings.width/3 + buttons_distance * i, buttons_pos_y,
                    image = 'buttons/small/button.png',
                    image_selected = 'buttons/small/button_active.png',
                    scale = buttons_scale,
                    text='',
                    arg=units_info[i][1],
                    text_color=BUTTONS_FONT_COLOR,
                    text_indent=settings.width/35,
                    text_scale=BUTTONS_FONT_SCALE,
                    text_size_y=1.3
                )
            )

            self.units_buttons_ico.append(
                image_label(
                    'world/units/ico/%s.png' % (units_info[i][0]),
                    settings.width/3 + buttons_distance * i, buttons_pos_y,
                    scale=buttons_scale
                )
            )

            self.units_buttons_load.append(
                label(
                    settings.width/3 + buttons_distance * i, buttons_pos_y,
                    self.units_buttons[i].image_obj.sprite.width, (self.units_buttons[i].image_obj.sprite.height/(i+1)),
                    (0, 0, 0), alpha=128
                )
            )

            self.units_buttons_time.append([10, 0.5, 10])

#-------------------------------------------------------------------------------
    def add_unit(self, type):
        if self.units_buttons_time[type][0] <= 0:
            get_obj_display('units').add_unit(type)
            self.units_buttons_time[type][0] = self.units_buttons_time[type][2]

    def update(self):
        if get_obj_display('game_rule').pause and not get_obj_display('game_rule').pause_settings:
            if self.pause_anim_time <= time.perf_counter():
                self.pause_anim_flag = not self.pause_anim_flag

                self.pause_anim_time = time.perf_counter() + self.pause_anim_delay

        else:
            for i in range(len(self.units_buttons_time)):
                if self.units_buttons_time[i][0] > 0:
                    self.units_buttons_time[i][0] -= self.units_buttons_time[i][1]

                self.units_buttons_load[i].rec.height = (self.units_buttons[i].image_obj.sprite.height/100)*self.units_buttons_time[i][0]

    def on_mouse_motion(self, x, y, dx, dy):
        if get_obj_other('setings_game').draw_gui and not get_obj_display('world').menu and not get_obj_display('game_rule').pause_settings:
            self.settings_button.on_mouse_motion(x, y, dx, dy)
            self.play_fast_button.on_mouse_motion(x, y, dx, dy)
            self.play_button.on_mouse_motion(x, y, dx, dy)
            self.pause_button.on_mouse_motion(x, y, dx, dy)

            for button in self.units_buttons:
                button.on_mouse_motion(x, y, dx, dy)

    def on_mouse_press(self, x, y, dx, dy):
        if get_obj_other('setings_game').draw_gui and not get_obj_display('world').menu and not get_obj_display('game_rule').pause_settings:
            self.settings_button.on_mouse_press(x, y, dx, dy)
            self.play_fast_button.on_mouse_press(x, y, dx, dy)
            self.play_button.on_mouse_press(x, y, dx, dy)
            self.pause_button.on_mouse_press(x, y, dx, dy)

            for button in self.units_buttons:
                button.on_mouse_press(x, y, dx, dy)

    def draw(self):
        if get_obj_other('setings_game').draw_gui and not get_obj_display('world').menu:
            drawp(self.settings_button)
            drawp(self.play_fast_button)
            drawp(self.play_button)
            drawp(self.pause_button)

            for button in self.units_buttons:
                button.draw()
            for button in self.units_buttons_ico:
                button.draw()
            for button in self.units_buttons_load:
                button.draw()

            if get_obj_display('game_rule').pause and self.pause_anim_flag and not get_obj_display('game_rule').pause_settings:
                self.pause_text.draw()
