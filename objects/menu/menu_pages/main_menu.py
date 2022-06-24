def add_main_menu(self):
    menu_buttons_distance = self.menu_buttons_distance

    self.menu_elements.append([])
    self.menu_elements[0].append(
        image_button(
            settings.width/1.3, settings.height - settings.height/2,
            image = 'buttons/big/button.png',
            image_selected = 'buttons/big/button_active.png',
            scale = settings.height/150,
            text='campaign',
            #function=play,
            arg='get_obj_display(\'select_map\').show = True',
            text_color=BUTTONS_FONT_COLOR,
            text_indent=settings.width/40,
            text_scale=BUTTONS_FONT_SCALE,
            text_size_y=1.3
        )
    )

    self.menu_elements[0].append(
        image_button(
            settings.width/1.3, settings.height - settings.height/2 - menu_buttons_distance,
            image = 'buttons/big/button.png',
            image_selected = 'buttons/big/button_active.png',
            scale = settings.height/150,
            text='sandbox',
            text_color=BUTTONS_FONT_COLOR,
            text_indent=settings.width/35,
            text_scale=BUTTONS_FONT_SCALE,
            text_size_y=1.3
        )
    )

    self.menu_elements[0].append(
        image_button(
            settings.width/1.3, settings.height - settings.height/2 - (menu_buttons_distance)*2,
            image = 'buttons/big/button.png',
            image_selected = 'buttons/big/button_active.png',
            scale = settings.height/150,
            text='settings',
            arg='get_obj_display(\'menu_class\').open_menu(1)',
            text_color=BUTTONS_FONT_COLOR,
            text_indent=settings.width/35,
            text_scale=BUTTONS_FONT_SCALE,
            text_size_y=1.3
        )
    )

    self.menu_elements[0].append(
        image_button(
            settings.width/1.3, settings.height - settings.height/2 - (menu_buttons_distance)*3,
            image = 'buttons/big/button.png',
            image_selected = 'buttons/big/button_active.png',
            scale = settings.height/150,
            text='exit',
            arg='exit()',
            text_color=BUTTONS_FONT_COLOR,
            text_indent=settings.width/35,
            text_scale=BUTTONS_FONT_SCALE,
            text_size_y=1.3
        )
    )

    self.menu_elements[0].append(
        image_button(
            settings.width/40, settings.height - settings.height/1.8 - (menu_buttons_distance)*2.8,
            image = 'buttons/small/button.png',
            image_selected = 'buttons/small/button_active.png',
            scale = settings.height/150,
            text='',
            arg='webbrowser.open_new(\'%s\')' % GIT_URL,
            text_color=BUTTONS_FONT_COLOR,
            text_indent=settings.width/35,
            text_scale=BUTTONS_FONT_SCALE,
            text_size_y=1.3
        )
    )

    self.menu_elements[0].append(
        image_label('ico/github.png', settings.width/40, settings.height - settings.height/1.8 - (menu_buttons_distance)*2.8, scale=settings.height/150)
    )
