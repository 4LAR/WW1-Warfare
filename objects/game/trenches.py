class trenches():
    def __init__(self):
        self.pos = []
        
        #self.pos.append(10)
        self.pos.append(70)
        self.pos.append(120)

        self.image = image_label('world/trenches/trenches_left.png', 0 , 0, scale=SCALE_WORLD)

    def draw(self):
        for pos in self.pos:
            self.image.sprite.x = get_obj_display('world').pos_with_world(pos) + get_obj_display('world').move_x + get_obj_display('world').map_offs[0]
            self.image.sprite.y = get_obj_display('world').map_offs[1] - get_obj_display('world').fov/2
            drawp(self.image)
