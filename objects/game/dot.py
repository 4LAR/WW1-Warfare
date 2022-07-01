class dot():
    def __init__(self):
        self.dot_list = []

        self.health = 1000

        self.images = [[], []]
        self.image_shadows = [[], []]

        for flip in range(2):
            for i in range(4):
                self.images[flip].append(
                    Image.open('assets/img/world/dot/%d.png' % (i + 1))
                )

                if flip == 0:
                    self.images[flip][i] = PIL_to_pyglet(self.images[flip][i], SCALE_WORLD)

                else:
                    self.images[flip][i] = PIL_to_pyglet(self.images[flip][i].transpose(Image.FLIP_LEFT_RIGHT), SCALE_WORLD)

                self.image_shadows[flip].append(
                    PIL_to_pyglet(image_transform_for_shadow('assets/img/world/dot/%d.png' % (i + 1), SHADOWS_COLOR), SCALE_WORLD),
                )

        self.state_health = self.health / (len(self.images[0]) - 1)

        #self.dot_list.append([flip, position_x, health])
        self.load()

    def load(self):
        self.dot_list = []
        for el in get_obj_display('world_save').dict['world']['dot']:
            self.dot_list.append(el)

    def draw(self):
        for dot in self.dot_list:
            x = get_obj_display('world').pos_with_world(dot[1]) + get_obj_display('world').move_x + get_obj_display('world').map_offs[0]
            y = get_obj_display('world').map_offs[1] - get_obj_display('world').fov/2 + (settings.height/2.7)/2

            if dot[2] > 0:
                state = 3 - int(dot[2] / self.state_health)

            else:
                state = len(self.images[0]) - 1

            self.images[dot[0]][state].x = x
            self.images[dot[0]][state].y = y
            drawp(self.images[dot[0]][state])

            if settings.game_options['game_shadows']:
                self.image_shadows[dot[0]][state].x = x
                self.image_shadows[dot[0]][state].y = y - self.image_shadows[dot[0]][state].height
                drawp(self.image_shadows[dot[0]][state])
