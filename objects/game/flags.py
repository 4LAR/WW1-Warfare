class parties_flag():
    def __init__(self):
        self.flag_list = []

        self.flagpole = image_label('world/flag/flagpole.png', 0, 0, scale=SCALE_WORLD)
        self.flagpole_shadow = PIL_to_pyglet(image_transform_for_shadow('assets/img/world/flag/flagpole.png', SHADOWS_COLOR), SCALE_WORLD)

        self.flags = []
        self.flags_shadows = []

        self.max_anim_tick = 4
        self.delay = 0.2
        self.time = time.perf_counter() + self.delay

        country = ['rus', 'britain', 'france', 'germany']
        for i in range(len(country)):
            self.flags.append([])
            self.flags_shadows.append([])
            for j in range(5):
                self.flags[i].append(image_label('world/flag/%s/%d.png' % (country[i], j + 1), 0, 0, scale=SCALE_WORLD))
                self.flags_shadows[i].append(PIL_to_pyglet(image_transform_for_shadow('assets/img/world/flag/%s/%d.png' % (country[i], j + 1), SHADOWS_COLOR), SCALE_WORLD))

        #self.flag_list.append([country, arentation, position, animation tick])
        self.load()

    def load(self):
        self.flag_list = []
        for el in get_obj_display('world_save').dict['world']['parties_flag']:
            self.flag_list.append(el)

    def update(self):
        if not get_obj_display('game_rule').pause:
            if self.time <= time.perf_counter():
                for i in range(len(self.flag_list)):
                    self.flag_list[i][3] += 1
                    if self.flag_list[i][3] > self.max_anim_tick:
                        self.flag_list[i][3] = 0

                self.time = time.perf_counter() + self.delay

    def draw(self):
        for flag in self.flag_list:
            x = get_obj_display('world').pos_with_world(flag[1]) + get_obj_display('world').move_x + get_obj_display('world').map_offs[0]
            y = get_obj_display('world').map_offs[1] - get_obj_display('world').fov/2 + (settings.height/2.7)/2

            self.flagpole.sprite.x = x - self.flagpole.sprite.width/2.2
            self.flagpole.sprite.y = y
            drawp(self.flagpole)

            self.flagpole_shadow.x = x - self.flagpole.sprite.width/2.2
            self.flagpole_shadow.y = y - self.flagpole_shadow.height
            drawp(self.flagpole_shadow)

            self.flags[flag[0]][flag[3]].sprite.x = x + self.flags[flag[0]][flag[3]].sprite.width/9
            self.flags[flag[0]][flag[3]].sprite.y = y + (self.flagpole.sprite.height - (self.flags[flag[0]][flag[3]].sprite.height*1.1))
            drawp(self.flags[flag[0]][flag[3]])

            self.flags_shadows[flag[0]][flag[3]].x = x + self.flags[flag[0]][flag[3]].sprite.width/9 - self.flagpole.sprite.width/2.2 + self.flagpole_shadow.width/1.8
            self.flags_shadows[flag[0]][flag[3]].y = y - (self.flagpole.sprite.height - (self.flags[flag[0]][flag[3]].sprite.height*1.1))
            drawp(self.flags_shadows[flag[0]][flag[3]])
