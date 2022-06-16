class trenches():
    def __init__(self):
        self.pos = []

        #self.pos.append([position_x, flip(right-0, left-1)])

        self.images = [
            PIL_to_pyglet(Image.open('assets/img/world/trenches/trenches.png'), SCALE_WORLD),
            PIL_to_pyglet(Image.open('assets/img/world/trenches/trenches.png').transpose(Image.FLIP_LEFT_RIGHT), SCALE_WORLD)
        ]

        self.load()
        
    def load(self):
        self.pos = []
        for el in get_obj_display('world_save').dict['world']['trenches']:
            self.pos.append(el)

    def draw(self):
        for pos in self.pos:
            self.images[pos[1]].x = get_obj_display('world').pos_with_world(pos[0]) + get_obj_display('world').move_x + get_obj_display('world').map_offs[0]
            self.images[pos[1]].y = get_obj_display('world').map_offs[1] - get_obj_display('world').fov/2
            drawp(self.images[pos[1]])
