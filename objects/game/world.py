
class world():
    def __init__(self, menu=False):
        self.menu = menu

        self.move_x = 0
        self.move_tick = 10

        self.map_offs = [0, 0]
        self.disp_pos = [0, 0]
        self.fov = 32

        self.collide_mouse = settings.width/10

        # загружаем картинку
        self.image_width = 250
        self.image = image_label('world/background.png', self.move_x + self.fov/2, -self.fov/2, scale=settings.height/240)
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

    def update(self):
        self.map_offs[0] = -(-settings.width/2 + self.disp_pos[0]) / self.fov
        self.map_offs[1] = -(-settings.height/2 + self.disp_pos[1]) / self.fov

        if not self.menu:
            if keyboard[key.A] or (self.disp_pos[0] < self.collide_mouse):
                self.move_left()
            elif keyboard[key.D] or (self.disp_pos[0] > settings.width - self.collide_mouse):
                self.move_right()

        # изменение аоложения картинки на экране
        self.image.sprite.x = self.move_x + self.map_offs[0] - self.fov
        self.image.sprite.y = self.map_offs[1] - self.fov/2

    def draw(self):
        drawp(self.image)
