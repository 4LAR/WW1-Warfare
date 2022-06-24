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
            arg='get_obj_display(\'menu_class\').open_menu(0)',
            text_color=BUTTONS_FONT_COLOR,
            text_indent=settings.width/40,
            text_scale=BUTTONS_FONT_SCALE,
            text_size_y=1.3
        )
    )
