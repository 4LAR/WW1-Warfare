class trenches():
    def __init__(self):
        self.pos = []
        self.pos.append(100)
        self.pos.append(700)
        self.pos.append(1200)

        self.image = image_label('world/trenches/trenches_left.png', 0 , 0, scale=settings.height/240)

    def draw(self):
        for pos in self.pos:
            self.image.sprite.x = pos + get_obj_display('world').move_x + get_obj_display('world').map_offs[0]
            self.image.sprite.y = get_obj_display('world').map_offs[1] - get_obj_display('world').fov/2
            drawp(self.image)
