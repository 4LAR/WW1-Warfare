
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

        self.menu_buttons_distance = settings.height/6.5

#-------------------------------MAIN-MENU---------------------------------------

        add_main_menu(self)

#---------------------------SETTINGS-MENU---------------------------------------

        add_settings_menu(self)

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
