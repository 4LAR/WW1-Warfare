class dot():
    def __init__(self):
        self.dot_list = []

        self.images = [
            image_label('world/dot/1.png', 0, 0, scale=SCALE_WORLD),
            image_label('world/dot/2.png', 0, 0, scale=SCALE_WORLD),
            image_label('world/dot/3.png', 0, 0, scale=SCALE_WORLD),
            image_label('world/dot/4.png', 0, 0, scale=SCALE_WORLD)
        ]

        self.image_shadows = [
            PIL_to_pyglet(image_transform_for_shadow('assets/img/world/dot/1.png', SHADOWS_COLOR), SCALE_WORLD),
            PIL_to_pyglet(image_transform_for_shadow('assets/img/world/dot/2.png', SHADOWS_COLOR), SCALE_WORLD),
            PIL_to_pyglet(image_transform_for_shadow('assets/img/world/dot/3.png', SHADOWS_COLOR), SCALE_WORLD),
            PIL_to_pyglet(image_transform_for_shadow('assets/img/world/dot/4.png', SHADOWS_COLOR), SCALE_WORLD)
        ]

        #self.dot_list.append([flip, position_x, state])
        self.load()
        
    def load(self):
        self.dot_list = []
        for el in get_obj_display('world_save').dict['world']['dot']:
            self.dot_list.append(el)

    def draw(self):
        for dot in self.dot_list:
            x = get_obj_display('world').pos_with_world(dot[1]) + get_obj_display('world').move_x + get_obj_display('world').map_offs[0]
            y = get_obj_display('world').map_offs[1] - get_obj_display('world').fov/2 + (settings.height/2.7)/2

            self.images[dot[2]].sprite.x = x
            self.images[dot[2]].sprite.y = y
            drawp(self.images[dot[2]])

            self.image_shadows[dot[2]].x = x
            self.image_shadows[dot[2]].y = y - self.image_shadows[dot[2]].height
            drawp(self.image_shadows[dot[2]])
