class units():
    def __init__(self):
        self.human_speed = SCALE_WORLD/2

        self.unit_list = [[], []]

        self.images = []
        self.images_shadows = []

        test_image = PIL_to_pyglet(Image.new("RGBA", (30, 40), (0, 0, 0, 255)), SCALE_WORLD/1.2)
        test_image_shadow = PIL_to_pyglet(Image.new("RGBA", (30, 40), (0, 0, 0, 0)), SCALE_WORLD/1.2)

        self.units_info = {}
        self.path = 'units_info.json'
        if not os.path.exists(self.path):
            load_units_info(self)

        else:
            self.units_info = read_dict(self.path.split('.')[0])

        # human
        self.images.append({})
        self.images_shadows.append({})

        unit_types = [
            ['run', 8]
        ]

        for type in range(len(unit_types)):
            self.images[0][unit_types[type][0]] = [[], []]
            self.images_shadows[0][unit_types[type][0]] = [[], []]
            for flip in range(2):
                for i in range(unit_types[type][1]):
                    self.images[0][unit_types[type][0]][flip].append(Image.open('assets/img/world/units/human/%s/%d.png' % (unit_types[type][0], i + 1)))
                    if flip == 0:
                        self.images[0][unit_types[type][0]][flip][i] = self.images[0][unit_types[type][0]][flip][i].transpose(Image.FLIP_LEFT_RIGHT)

                    #self.images_shadows[0][unit_types[type][0]][flip].append(PIL_to_pyglet(image_transform_for_shadow(self.images[0][unit_types[type][0]][flip][i], SHADOWS_COLOR, True), SCALE_WORLD/1.2))

                    self.images[0][unit_types[type][0]][flip][i] = PIL_to_pyglet(self.images[0][unit_types[type][0]][flip][i], SCALE_WORLD/1.2)

        # human with gas
        self.images.append([test_image])
        self.images_shadows.append([test_image_shadow])

        # sniper
        self.images.append([test_image])
        self.images_shadows.append([test_image_shadow])

        # mortar man
        self.images.append([test_image])
        self.images_shadows.append([test_image_shadow])

        # tank
        self.images.append({})
        self.images_shadows.append({})

        unit_types = [
            ['a7v', 5],
            ['mark-1', 5]
        ]

        for type in range(len(unit_types)):
            self.images[4][unit_types[type][0]] = [[], []]
            self.images_shadows[4][unit_types[type][0]] = [[], []]
            for flip in range(2):
                for i in range(unit_types[type][1]):
                    self.images[4][unit_types[type][0]][flip].append(Image.open('assets/img/world/units/%s/%d.png' % (unit_types[type][0], i + 1)))
                    if flip == 0:
                        self.images[4][unit_types[type][0]][flip][i] = self.images[4][unit_types[type][0]][flip][i].transpose(Image.FLIP_LEFT_RIGHT)

                    self.images_shadows[4][unit_types[type][0]][flip].append(PIL_to_pyglet(image_transform_for_shadow(self.images[4][unit_types[type][0]][flip][i], SHADOWS_COLOR, True), SCALE_WORLD/1.2))

                    self.images[4][unit_types[type][0]][flip][i] = PIL_to_pyglet(self.images[4][unit_types[type][0]][flip][i], SCALE_WORLD/1.2)

    def add_unit(self, type=0, flip=0):
        y = random.randint(
            int(-settings.height/10),
            int(settings.height/10)
        )

        country = get_obj_display('world').country if flip == 0 else get_obj_display('world').enemy

        if type == 0:
            #self.unit_list.append([human(0, 0), 0, y, False])
            self.unit_list[flip].append([unit(0, y, self.images[0]['run'][flip], self.images_shadows[0]['run'][flip], self.units_info[country][type], 0, flip), y])

        elif type == 1:
            self.unit_list[flip].append([unit(0, y, self.images[0], self.images_shadows[0], self.units_info[country][type], 1, flip), y])

        elif type == 2:
            self.unit_list[flip].append([unit(0, y, self.images[0], self.images_shadows[0], self.units_info[country][type], 2, flip), y])

        elif type == 3:
            self.unit_list[flip].append([unit(0, y, self.images[0], self.images_shadows[0], self.units_info[country][type], 3, flip), y])

        elif type == 4:
            self.unit_list[flip].append([unit(0, y, self.images[4][self.units_info[country][type]['image']][flip], self.images_shadows[4][self.units_info[country][type]['image']][flip], self.units_info[country][type], 4, flip), y])

        self.unit_list[flip] = sorted(self.unit_list[flip], key=lambda tup: tup[1], reverse=True)

        if flip == 0:
            get_obj_display('game_info').info['unit_spawned'] += 1

        else:
            get_obj_display('game_info').info['enemy_unit_spawned'] += 1

    def update(self):
        if settings.game_options['game_clear_dead_units']:
            for flip in range(2):
                for i in range(len(self.unit_list[flip]) - 1, -1 ,-1):
                    if self.unit_list[flip][i][0].health <= 0:
                        self.unit_list[flip].pop(i)

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
