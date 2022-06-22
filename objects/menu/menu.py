
# text color
# HEX: #B6B3A6
# RGB: (182, 179, 166)
# font: urod.ttf

GIT_URL = 'https://github.com/4LAR/WW1-Warfare'

class menu_class():
    def __init__(self):

        # загружаем картинку
        self.image_logo = image_label('logo_game.png', settings.width/1.28, settings.height - settings.height/3, scale=settings.height/150)

        # кнопки главного меню
        self.menu_selected = 0
        self.menu_elements = []

        menu_buttons_distance = settings.height/6.5

#-------------------------------MAIN-MENU---------------------------------------

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

#---------------------------SETTINGS-MENU---------------------------------------

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

#-------------------------------------------------------------------------------

    def open_menu(self, id):
        self.menu_selected = id

    def on_mouse_motion(self, x, y, dx, dy):
        if not get_obj_display('select_map').show:
            for element in self.menu_elements[self.menu_selected]:
                try:
                    element.on_mouse_motion(x, y, dx, dy)
                except:
                    pass

    def on_mouse_press(self, x, y, dx, dy):
        if not get_obj_display('select_map').show:
            for element in self.menu_elements[self.menu_selected]:
                try:
                    element.on_mouse_press(x, y, dx, dy)
                except:
                    pass

    def draw(self):
        if self.menu_selected == 0:
            drawp(self.image_logo)

        for element in self.menu_elements[self.menu_selected]:
            element.draw()

FIRST_RUN = True

def menu():
    load_cursor('cursor/default.png', SCALE_WORLD)
    show_cursor()
    global FIRST_RUN

    clear_display()
    add_game_classes(True)
    add_display(menu_class())
    add_display(select_map())
    if FIRST_RUN:
        FIRST_RUN = not FIRST_RUN
        add_display(breathing_label(0, 0, settings.width, settings.height, (0, 0, 0), 0, delay=0.01, for_from=255, for_before=0, tick=-5))
