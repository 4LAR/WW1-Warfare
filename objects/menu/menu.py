
# text color
# HEX: #B6B3A6
# RGB: (182, 179, 166)
# font: pixel.ttf

class menu_class():
    def __init__(self):

        # загружаем картинку
        self.image_logo = image_label('logo_game.png', settings.width/1.28, settings.height - settings.height/3, scale=settings.height/150)

        # кнопки главного меню
        self.menu_selected = 0
        self.menu_elements = []

        self.menu_elements.append([])
        menu_buttons_distance = settings.height/6.5
        self.menu_elements[0].append(
            image_button(
                settings.width/1.3, settings.height - settings.height/1.8,
                image = 'buttons/big/button.png',
                image_selected = 'buttons/big/button_active.png',
                scale = settings.height/150,
                text='campaign',
                function=play,
                text_color=(182, 179, 166, 255),
                text_indent=settings.width/35,
                text_scale=6,
                text_size_y=1.9
            )
        )

        self.menu_elements[0].append(
            image_button(
                settings.width/1.3, settings.height - settings.height/1.8 - menu_buttons_distance,
                image = 'buttons/big/button.png',
                image_selected = 'buttons/big/button_active.png',
                scale = settings.height/150,
                text='sandbox',
                text_color=(182, 179, 166, 255),
                text_indent=settings.width/35,
                text_scale=6,
                text_size_y=1.9
            )
        )

        self.menu_elements[0].append(
            image_button(
                settings.width/1.3, settings.height - settings.height/1.8 - (menu_buttons_distance)*2,
                image = 'buttons/big/button.png',
                image_selected = 'buttons/big/button_active.png',
                scale = settings.height/150,
                text='settings',
                text_color=(182, 179, 166, 255),
                text_indent=settings.width/35,
                text_scale=6,
                text_size_y=1.9
            )
        )

    def on_mouse_motion(self, x, y, dx, dy):
        for element in self.menu_elements[self.menu_selected]:
            element.on_mouse_motion(x, y, dx, dy)

    def on_mouse_press(self, x, y, dx, dy):
        for element in self.menu_elements[self.menu_selected]:
            element.on_mouse_press(x, y, dx, dy)

    def draw(self):
        if self.menu_selected == 0:
            drawp(self.image_logo)

        for element in self.menu_elements[self.menu_selected]:
            drawp(element)

def menu():
    add_display(world(menu=True))
    add_display(menu_class())
