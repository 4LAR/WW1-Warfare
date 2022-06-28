class units():
    def __init__(self):
        self.human_speed = SCALE_WORLD/2

        self.human_list = [[], []]
        self.tank_list = [[], []]

        self.images = []
        self.images_shadows = []

        # human type 1
        self.images.append([])
        self.images_shadows.append([])

        # human type 2
        self.images.append([])
        self.images_shadows.append([])

        # tank

        self.images.append([[], []])
        self.images_shadows.append([[], []])

        type = 1
        flip = 0

        tanks_types = [
            ['mark-1', 5],
            ['a7v', 5]
        ]

        for j in range(2):
            for i in range(tanks_types[type][1]):
                self.images[2][j].append(Image.open('assets/img/world/units/%s/%d.png' % (tanks_types[type][0], i + 1)))
                if j == 0:
                    self.images[2][j][i] = self.images[2][j][i].transpose(Image.FLIP_LEFT_RIGHT)

                self.images_shadows[2][j].append(PIL_to_pyglet(image_transform_for_shadow(self.images[2][j][i], SHADOWS_COLOR, True), SCALE_WORLD/1.2))

                self.images[2][j][i] = PIL_to_pyglet(self.images[2][j][i], SCALE_WORLD/1.2)

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
            self.tank_list[1].append([tank(0, y, self.images[2][1], self.images_shadows[2][1], 1, flip=1), y])
            pass

        elif type == 2:
            self.tank_list[0].append([tank(0, y, self.images[2][0], self.images_shadows[2][0], 1), y])

            self.tank_list[0] = sorted(self.tank_list[0], key=lambda tup: tup[1], reverse=True)

    def draw(self):

        x = get_obj_display('world').move_x + get_obj_display('world').map_offs[0]
        y = get_obj_display('world').map_offs[1] - get_obj_display('world').fov/2 + (settings.height/2.7)/2

        for i in range(2):
            for tank in self.tank_list[i]:
                if not get_obj_display('game_rule').pause:
                    tank[0].update()
                    #threading.Thread(target=tank.update).start()
                    #asyncio.run(tank.update())

                tank[0].draw(x, y)

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
