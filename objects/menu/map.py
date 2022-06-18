class select_map():
    def __init__(self):

        buttons_scale = settings.height/150

        self.show = False

        self.background = label(0, 0, settings.width, settings.height, (0, 0, 0), alpha=128)

        self.image = image_label('map.png', 0, 0, scale=SCALE_WORLD * 1.2)
        self.image.sprite.x = (settings.width - self.image.sprite.width)/2
        self.image.sprite.y = (settings.height - self.image.sprite.height)/2

        self.map_pixel_size = [
            self.image.sprite.width / 232,
            self.image.sprite.height / 186
        ]

        self.back_button = image_button(
            settings.width - settings.width/6, settings.height - settings.height/5.5,
            image = 'buttons/small/button.png',
            image_selected = 'buttons/small/button_active.png',
            scale = buttons_scale,
            text='',
            arg='get_obj_display(\'select_map\').show = False',
            text_color=BUTTONS_FONT_COLOR,
            text_indent=settings.width/35,
            text_scale=BUTTONS_FONT_SCALE,
            text_size_y=1.3
        )

        self.back_button_ico = image_label('buttons/cross.png', settings.width - settings.width/6 + self.back_button.image_obj.sprite.width/44, settings.height - settings.height/5.5, scale=buttons_scale)

        self.mission_list = [
            #[x, y, map_name, mission_name]
            [100, 100, 'test_summer', 'test'],
            [140, 90, 'test_autum', 'test'],
            [10, 170, 'assets', 'test']
        ]

        self.mission_buttons = []
        for mission in self.mission_list:
            self.mission_buttons.append(
                image_button(
                    self.image.sprite.x + (mission[0] * self.map_pixel_size[0]), self.image.sprite.y + (mission[1] * self.map_pixel_size[1]),
                    image = 'point.png',
                    image_selected = 'point.png',
                    scale = SCALE_WORLD * 1.2,
                    text='',
                    #arg='play(\'%s\')' % mission[2],
                    arg='play_breath(\'%s\')' % mission[2],
                    text_color=BUTTONS_FONT_COLOR,
                    text_indent=settings.width/40,
                    text_scale=BUTTONS_FONT_SCALE,
                    text_size_y=1.3
                )
            )

    def on_mouse_motion(self, x, y, dx, dy):
        if self.show:
            self.back_button.on_mouse_motion(x, y, dx, dy)

            for button in self.mission_buttons:
                button.on_mouse_motion(x, y, dx, dy)

    def on_mouse_press(self, x, y, dx, dy):
        if self.show:
            self.back_button.on_mouse_press(x, y, dx, dy)

            for button in self.mission_buttons:
                button.on_mouse_press(x, y, dx, dy)

    def draw(self):
        if self.show:
            self.background.draw()
            drawp(self.image)
            self.back_button.draw()
            drawp(self.back_button_ico)

            for button in self.mission_buttons:
                button.draw()
