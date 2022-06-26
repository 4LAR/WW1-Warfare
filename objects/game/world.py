
class world():
    def __init__(self, menu=False):
        self.menu = menu

        self.move_x = 0
        self.move_tick = 10

        self.map_offs = [0, 0]
        self.disp_pos = [0, 0]
        self.fov = 32

        self.collide_mouse = settings.width/10
        self.collide_mouse_y = [settings.height/6, settings.height - settings.height/6]
        self.collide_mouse_bool = False

        self.cursor_images = [
            PIL_to_pyglet_imageData(Image.open('assets/img/cursor/default.png')),
            PIL_to_pyglet_imageData(Image.open('assets/img/cursor/move.png').transpose(Image.FLIP_LEFT_RIGHT)),
            PIL_to_pyglet_imageData(Image.open('assets/img/cursor/move.png'))
        ]

        for i in range(len(self.cursor_images)):
            self.cursor_images[i] = load_cursor(self.cursor_images[i], SCALE_WORLD, raw_image=True, return_cursor=True)

        # autum, summer
        self.season = get_obj_display('world_save').dict['world']['season']

        # загружаем картинку
        self.image_width = 250
        self.image = image_label('world/world/%s/background_ground.png' % self.season, self.move_x + self.fov/2, -self.fov/2, scale=SCALE_WORLD)
        self.image_ground = image_label('world/world/%s/background_ground_deco.png' % self.season, self.move_x + self.fov/2, -self.fov/2, scale=SCALE_WORLD)
        self.image_forest = image_label('world/world/%s/background_forest.png' % self.season, self.move_x + self.fov/2, -self.fov/2, scale=SCALE_WORLD)
        self.image_sky = image_label('world/world/background_sky.png', self.move_x + self.fov/2, -self.fov/2, scale=SCALE_WORLD)

        self.pixel_size = self.image.sprite.width / self.image_width

        # константы
        self.move_min = -self.image.sprite.width + settings.width + self.fov * 2
        self.move_max = -self.fov/2

    def pos_with_world(self, x):
        return self.pixel_size * x

    # для паралакса
    def on_mouse_motion(self, x, y, dx, dy):
        self.disp_pos = [x, y]

    def on_mouse_drag(self, x, y, dx, dy, buttons, modifiers):
        self.disp_pos = [x, y]

    # смещение карты влево
    def move_left(self):
        if (self.move_max > self.move_x + self.move_tick):
            self.move_x += self.move_tick

    # смещение карты направо
    def move_right(self):
        if (self.move_min < self.move_x - self.move_tick):
            self.move_x -= self.move_tick

    def on_key_press(self, symbol, modifiers):
        if symbol == pyglet.window.key.ESCAPE:
            if not self.menu:
                if get_obj_display('game_rule').pause_settings:
                    get_obj_display('game_rule')._unpause_settings()
                else:
                    get_obj_display('game_rule')._pause_settings()

            else:
                if get_obj_display('menu_class').menu_selected == 0:
                    exit()

                else:
                    get_obj_display('menu_class').save_settings()

            return pyglet.event.EVENT_HANDLED

    def update(self):
        if settings.game_options['game_parallax']:
            self.map_offs[0] = -(-settings.width/2 + self.disp_pos[0]) / self.fov
            self.map_offs[1] = -(-settings.height/2 + self.disp_pos[1]) / self.fov
        else:
            self.map_offs[0] = 0
            self.map_offs[1] = 0

        if not self.menu and not get_obj_display('game_rule').pause_settings:
            if keyboard[key.A] or ((self.disp_pos[0] < self.collide_mouse) and (self.collide_mouse_y[0] < self.disp_pos[1] < self.collide_mouse_y[1])):
                self.move_left()
            elif keyboard[key.D] or ((self.disp_pos[0] > settings.width - self.collide_mouse) and (self.collide_mouse_y[0] < self.disp_pos[1] < self.collide_mouse_y[1])):
                self.move_right()

            if ((self.disp_pos[0] < self.collide_mouse) and (self.collide_mouse_y[0] < self.disp_pos[1] < self.collide_mouse_y[1])):
                if not self.collide_mouse_bool:
                    self.collide_mouse_bool = True
                    window.set_mouse_cursor(self.cursor_images[1])

            elif ((self.disp_pos[0] > settings.width - self.collide_mouse) and (self.collide_mouse_y[0] < self.disp_pos[1] < self.collide_mouse_y[1])):
                if not self.collide_mouse_bool:
                    self.collide_mouse_bool = True
                    window.set_mouse_cursor(self.cursor_images[2])

            else:
                if self.collide_mouse_bool:
                    self.collide_mouse_bool = False
                    window.set_mouse_cursor(self.cursor_images[0])

        # изменение аоложения картинки на экране
        self.image.sprite.x = self.move_x + self.map_offs[0] - self.fov
        self.image.sprite.y = self.map_offs[1] - self.fov/2

        self.image_sky.sprite.x = self.move_x + (self.map_offs[0]*0.8) - self.fov
        self.image_sky.sprite.y = (self.map_offs[1]*0.8) - self.fov/2

        self.image_ground.sprite.x = self.move_x + (self.map_offs[0]*0.9) - self.fov
        self.image_ground.sprite.y = (self.map_offs[1]*0.8) - self.fov/2 + settings.height/20

        self.image_forest.sprite.x = self.move_x + (self.map_offs[0]*0.9) - self.fov
        self.image_forest.sprite.y = (self.map_offs[1]*0.8) - self.fov/2 + settings.height/25

    def draw(self):
        drawp(self.image_sky)
        drawp(self.image_forest)
        drawp(self.image_ground)
        drawp(self.image)
