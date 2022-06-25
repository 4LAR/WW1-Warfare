def add_settings_menu(self):
    menu_buttons_distance = self.menu_buttons_distance

    self.menu_elements.append([])
    self.menu_elements[1].append(
        image_button(
            settings.width/1.3, settings.height - settings.height/2 - (menu_buttons_distance)*3,
            image = 'buttons/big/button.png',
            image_selected = 'buttons/big/button_active.png',
            scale = settings.height/150,
            text='back',
            arg='get_obj_display(\'menu_class\').save_settings()',
            text_color=BUTTONS_FONT_COLOR,
            text_indent=settings.width/40,
            text_scale=BUTTONS_FONT_SCALE,
            text_size_y=1.3
        )
    )

    '''self.menu_elements[1].append(
        input_label_image(
            settings.width/40, settings.height - settings.height/2 - (menu_buttons_distance)*(-1),
            'buttons/input_small/input.png',
            'buttons/input_small/input.png',

            scale=settings.height/160,
            color_text=BUTTONS_FONT_COLOR,
            text='width',
            pre_text='1600',
            font='urod.ttf',
            text_indent=settings.width/9,
            text_input_indent=settings.width/9
        )
    )'''


    self.menu_elements[1].append(
        image_flag(
            settings.width/40, settings.height - settings.height/2 - (menu_buttons_distance)*0,
            image='buttons/flag/flag.png',
            image_flag='buttons/flag/flag_selected.png',
            image_selected_flag='buttons/flag/flag_selected_active.png',
            image_selected='buttons/flag/flag_active.png',
            scale=settings.height/160,
            function_bool = True,
            arg='pass',

            text='cursor',
            text_color = BUTTONS_FONT_COLOR,
            text_scale= BUTTONS_FONT_SCALE,
            font='urod.ttf',
            text_indent=settings.width/9,
            text_size_y=1.3,

            flag = settings.game_options['game_cursor']

        )
    )

    self.menu_elements[1].append(
        image_flag(
            settings.width/40, settings.height - settings.height/2 - (menu_buttons_distance)*1,
            image='buttons/flag/flag.png',
            image_flag='buttons/flag/flag_selected.png',
            image_selected_flag='buttons/flag/flag_selected_active.png',
            image_selected='buttons/flag/flag_active.png',
            scale=settings.height/160,
            function_bool = True,
            arg='pass',

            text='parallax',
            text_color = BUTTONS_FONT_COLOR,
            text_scale= BUTTONS_FONT_SCALE,
            font='urod.ttf',
            text_indent=settings.width/9,
            text_size_y=1.3,

            flag = settings.game_options['game_parallax']

        )
    )

    self.menu_elements[1].append(
        image_flag(
            settings.width/40, settings.height - settings.height/2 - (menu_buttons_distance)*2,
            image='buttons/flag/flag.png',
            image_flag='buttons/flag/flag_selected.png',
            image_selected_flag='buttons/flag/flag_selected_active.png',
            image_selected='buttons/flag/flag_active.png',
            scale=settings.height/160,
            function_bool = True,
            arg='pass',

            text='shadows',
            text_color = BUTTONS_FONT_COLOR,
            text_scale= BUTTONS_FONT_SCALE,
            font='urod.ttf',
            text_indent=settings.width/9,
            text_size_y=1.3,

            flag = settings.game_options['game_shadows']

        )
    )
