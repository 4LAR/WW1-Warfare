class units():
    def __init__(self):
        self.human_speed = SCALE_WORLD/2

        self.unit_list = [[], []]

        self.images = []
        self.images_shadows = []

        # human type 1
        self.images.append([])
        self.images_shadows.append([])

        # human type 2
        self.images.append([])
        self.images_shadows.append([])

        # tank
        self.images.append([])
        self.images_shadows.append([])

        unit_types = [
            ['mark-1', 5],
            ['a7v', 5]
        ]

        for type in range(len(unit_types)):
            self.images[2].append([[], []])
            self.images_shadows[2].append([[], []])
            for flip in range(2):
                for i in range(unit_types[type][1]):
                    self.images[2][type][flip].append(Image.open('assets/img/world/units/%s/%d.png' % (unit_types[type][0], i + 1)))
                    if flip == 0:
                        self.images[2][type][flip][i] = self.images[2][type][flip][i].transpose(Image.FLIP_LEFT_RIGHT)

                    self.images_shadows[2][type][flip].append(PIL_to_pyglet(image_transform_for_shadow(self.images[2][type][flip][i], SHADOWS_COLOR, True), SCALE_WORLD/1.2))

                    self.images[2][type][flip][i] = PIL_to_pyglet(self.images[2][type][flip][i], SCALE_WORLD/1.2)

    def add_unit(self, type=0):
        y = random.randint(
            int(-settings.height/10),
            int(settings.height/10)
        )
        if type == 0:
            #self.human_list.append([human(0, 0), 0, y, False])
            pass

        elif type == 1:
            #self.human_list.append([human(0, 0, 'germany', 1, 2, 1, 1, 2), 0, y, False])
            self.unit_list[1].append([unit(0, y, self.images[2][0][1], self.images_shadows[2][0][1], 0, flip=1), y])
            pass

        elif type == 2:
            self.unit_list[0].append([unit(0, y, self.images[2][1][0], self.images_shadows[2][1][0], 0), y])

            self.unit_list[0] = sorted(self.unit_list[0], key=lambda tup: tup[1], reverse=True)

    def draw(self, down=False):

        x = get_obj_display('world').move_x + get_obj_display('world').map_offs[0]
        y = get_obj_display('world').map_offs[1] - get_obj_display('world').fov/2 + (settings.height/2.7)/2

        for i in range(2):
            for unit in self.unit_list[i]:
                if (unit[0].pos_y < 0 and down) or (unit[0].pos_y > 0 and not down):
                    if not get_obj_display('game_rule').pause:
                        unit[0].update()
                        #threading.Thread(target=tank.update).start()
                        #asyncio.run(tank.update())

                    unit[0].draw(x, y)
'''
        for i in range(2):
            for human in self.human_list[1]:
                if not get_obj_display('game_rule').pause:
                    if not human[3]:
                        human[1] += self.human_speed
                        if (x + human[1] > get_obj_display('world').image.sprite.width):
                            human[3] = True
                        human[0].update_pos(x + human[1], y + human[2])

                    #human[0].update()
                    #threading.Thread(target=human[0].update).start()
                    #multiprocessing.Process(target=human[0].update).start()
                    asyncio.run(human[0].update())

                    human[0].draw()
'''

class units_down():
    def draw(self):
        get_obj_display('units').draw(True)
