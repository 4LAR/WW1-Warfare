class clouds():
    def __init__(self):

        self.image = image_label('world/world/clouds.png', 0, 0, scale=SCALE_WORLD, alpha=200)
        self.image_width = 250

        self.move_max = self.image_width - 0.01
        self.move_x = [0, self.move_max]

        self.move_tick = 0.01

    def update(self):
        if not get_obj_display('game_rule').pause:
            for i in range(len(self.move_x)):
                self.move_x[i] -= self.move_tick
                if self.move_x[i] < -self.move_max:
                    self.move_x[i] = self.move_max

    def draw(self):
        for move in self.move_x:
            self.image.sprite.x = get_obj_display('world').pos_with_world(move) + get_obj_display('world').move_x + get_obj_display('world').map_offs[0]
            self.image.sprite.y = get_obj_display('world').map_offs[1] - get_obj_display('world').fov/2
            drawp(self.image)
