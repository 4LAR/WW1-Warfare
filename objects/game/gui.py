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
        self.units_text_money = []

        # world/units/ico/
        self.units_info = [
            # [0 image ico, 1 function, 2 money, 3 timer tick, 4 timer count tick]
            ['human', 'get_obj_display(\'gui\').add_unit(0)', 10, 0.5, 100],           # human
            ['human_with_mask', 'get_obj_display(\'gui\').add_unit(1)', 15, 0.5, 200], #  human with gas
            ['none', 'get_obj_display(\'gui\').add_unit(2)', 15, 0.5, 200],            # sniper
            ['none', 'get_obj_display(\'gui\').add_unit(3)', 15, 0.5, 200],            # mortar man
            ['tank', 'get_obj_display(\'gui\').add_unit(4)', 100, 0.5, 1000],           # tank
            ['none', 'print(\'bomb\')', 100, 0.5, 1500],                                # bomb
            ['none', 'print(\'gas bomb\')', 120, 0.5, 2000]                             # gas bomb

        ]

        buttons_pos_y = settings.height/60
        buttons_pos_x = settings.width/4

        self.money_background = image_label(
            'buttons/big/button.png',
            buttons_pos_x + buttons_distance * (len(self.units_info) + 1), buttons_pos_y,
            scale=buttons_scale
        )

        self.text_money = text_label(
            buttons_pos_x + buttons_distance * (len(self.units_info) + 1) + self.money_background.sprite.width/2,
            buttons_pos_y + self.money_background.sprite.height/1.5,
            text='None',
            color=BUTTONS_FONT_COLOR,
            size=int(buttons_scale * 15),
            load_font=True,
            font='urod.ttf',
            anchor_x='center',
            anchor_y='center'
        )

        for i in range(len(self.units_info)):
            self.units_buttons.append(
                image_button(
                    buttons_pos_x + buttons_distance * i, buttons_pos_y,
                    image = 'buttons/small/button.png',
                    image_selected = 'buttons/small/button_active.png',
                    scale = buttons_scale,
                    text='',
                    arg=self.units_info[i][1],
                    text_color=BUTTONS_FONT_COLOR,
                    text_indent=settings.width/35,
                    text_scale=BUTTONS_FONT_SCALE,
                    text_size_y=1.3
                )
            )

            self.units_buttons_ico.append(
                image_label(
                    'world/units/ico/%s.png' % (self.units_info[i][0]),
                    buttons_pos_x + buttons_distance * i, buttons_pos_y,
                    scale=buttons_scale
                )
            )

            self.units_buttons_load.append(
                label(
                    buttons_pos_x + buttons_distance * i, buttons_pos_y,
                    self.units_buttons[i].image_obj.sprite.width, (self.units_buttons[i].image_obj.sprite.height/(i+1)),
                    (0, 0, 0), alpha=128
                )
            )

            self.units_text_money.append(
                text_label(
                    buttons_pos_x + buttons_distance * i + self.units_buttons[i].image_obj.sprite.width/2, buttons_pos_y + self.units_buttons[i].image_obj.sprite.height * 1.3,
                    text=str(self.units_info[i][2]),
                    color=BUTTONS_FONT_COLOR,
                    size=int(buttons_scale * 10),
                    load_font=True,
                    font='urod.ttf',
                    anchor_x='center',
                    use = False
                )
            )

            self.units_buttons_time.append([0, self.units_info[i][3], self.units_info[i][4]])

#-------------------------------------------------------------------------------
    def add_unit(self, type):
        if self.units_buttons_time[type][0] <= 0 and get_obj_display('game_rule').money >= self.units_info[type][2]:
            get_obj_display('units').add_unit(type)
            self.units_buttons_time[type][0] = self.units_buttons_time[type][2]

            get_obj_display('game_rule').money -= self.units_info[type][2]
            get_obj_display('game_info').info['money_spent'] += self.units_info[type][2]

    def update(self):
        if get_obj_display('game_rule').pause and not get_obj_display('game_rule').pause_settings:
            if self.pause_anim_time <= time.perf_counter():
                self.pause_anim_flag = not self.pause_anim_flag

                self.pause_anim_time = time.perf_counter() + self.pause_anim_delay

        else:
            for i in range(len(self.units_buttons_time)):
                if self.units_buttons_time[i][0] > 0:
                    self.units_buttons_time[i][0] -= self.units_buttons_time[i][1]

                self.units_buttons_load[i].rec.height = (self.units_buttons[i].image_obj.sprite.height/self.units_buttons_time[i][2])*self.units_buttons_time[i][0]

        self.text_money.label.text = str(get_obj_display('game_rule').money)

    def on_mouse_motion(self, x, y, dx, dy):
        if get_obj_other('setings_game').draw_gui and not get_obj_display('world').menu and not get_obj_display('game_rule').pause_settings:
            self.settings_button.on_mouse_motion(x, y, dx, dy)
            self.play_fast_button.on_mouse_motion(x, y, dx, dy)
            self.play_button.on_mouse_motion(x, y, dx, dy)
            self.pause_button.on_mouse_motion(x, y, dx, dy)

            for i in range(len(self.units_buttons)):
                if self.units_buttons[i].on_mouse_motion(x, y, dx, dy):
                    self.units_text_money[i].use = True

                else:
                    self.units_text_money[i].use = False

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
            for button in self.units_text_money:
                button.draw()

            self.money_background.draw()
            self.text_money.draw()

            if settings.game_options['game_map_battle_state']:
                line_pos_y = int(settings.height/200)
                line_pos_x = int(settings.width/10)
                line_size = settings.width
                line_tick = line_size / get_obj_display('world').image_width
                draw_line(
                    [line_pos_x, line_pos_y],
                    [settings.width - line_pos_x, line_pos_y]
                )

                draw_line(
                    [line_pos_x, line_pos_y],
                    [int(line_pos_x + (line_tick*get_obj_display('rope').rope_pos)) - line_pos_x, line_pos_y],
                    (0, 0, 128)
                )

                draw_line(
                    [settings.width - line_pos_x, line_pos_y],
                    [int(line_pos_x + (line_tick*get_obj_display('rope').rope_pos)) - line_pos_x, line_pos_y],
                    (128, 0, 0)
                )

            if get_obj_display('game_rule').pause and self.pause_anim_flag and not get_obj_display('game_rule').pause_settings and not get_obj_display('game_rule').end_game:
                self.pause_text.draw()
