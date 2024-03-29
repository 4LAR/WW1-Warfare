
class unit():
    def __init__(self, x, y, images, images_shadows, unit_dict, type=0, flip=0):
        # types
        # 0 human
        # 1 human with gas
        # 2 sniper
        # 3 mortar man
        # 4 tank
        self.type = type

        # 0 left to right
        # 1 right to left
        self.flip = flip

        self.images = images
        self.images_shadows = images_shadows

        self.health = unit_dict['health']
        self.damage = unit_dict['demage']
        self.delay_shoot = unit_dict['delay_shoot']
        self.speed = settings.width / unit_dict['speed']
        self.unit_name = unit_dict['name']
        self.id = unit_dict['id']
        self.priority = unit_dict['priority']

        self.unit_text = text_label(
            0, 0,
            text='None',
            color=BUTTONS_FONT_COLOR,
            size=int(((settings.height/150)/1.5) * 10),
            load_font=True,
            font='urod.ttf',
            anchor_x='center'
        )

        self.stopline_bool = False
        self.dot = False
        self.stop = False

        self.pos_x = (-self.images[0].width + x) if (flip == 0) else (get_obj_display('world').image.sprite.width + x)
        self.pos_y = y

        if flip:
            self.speed = -self.speed

        self.state = 0

        if self.type == 4:
            self.state_health = self.health / (len(self.images) - 1)

        self.distance = self.images[0].width / 2

        self.time_shoot = time.perf_counter() + self.delay_shoot

    def update(self):

        if settings.game_options['game_unit_info']:
            self.unit_text.label.text = "(%d) %s" % (self.health, self.unit_name)

        if not self.stop and self.health > 0 and not self.dot:
            self.pos_x += self.speed

            #if (
            #    ((self.pos_x > get_obj_display('world').image.sprite.width - (self.images[0].width * 2)) and self.flip == 0) or
            #    (self.pos_x < (self.images[0].width)) and self.flip == 1):
            #    self.stop = True

        if (
            (self.flip == 0 and (self.pos_x + self.images[0].width + self.distance > get_obj_display('world').pos_with_world(get_obj_display('dot').dot_list[1][1]))) or
            (self.flip == 1 and (self.pos_x - self.distance < get_obj_display('world').pos_with_world(get_obj_display('dot').dot_list[0][1]) + get_obj_display('dot').images[0][0].width))
            ):
            self.dot = True

        if (((self.pos_x + self.images[0].width + self.distance > get_obj_display('world').pos_with_world(get_obj_display('rope').rope_pos)) and self.flip == 0) or
            ((self.pos_x - self.distance < get_obj_display('world').pos_with_world(get_obj_display('rope').rope_pos)) and self.flip == 1)):

            self.stop = True
            self.stopline_bool = True

        else:
            self.stop = False
            self.stopline_bool = False

        if self.time_shoot <= time.perf_counter():
            enemy_list = []
            enemy_country = 1 if (self.flip == 0) else 0
            if self.health > 0 and ((self.stopline_bool and len(get_obj_display('units').unit_list[enemy_country]) > 0) or self.dot):

                if not self.dot:
                    for priority in self.priority:
                        for i in range(len(get_obj_display('units').unit_list[enemy_country])):
                            if (get_obj_display('units').unit_list[enemy_country][i][0].health > 0 and
                                get_obj_display('units').unit_list[enemy_country][i][0].stopline_bool and
                                get_obj_display('units').unit_list[enemy_country][i][0].id == priority):
                                enemy_list.append(i)

                    if len(enemy_list) > 0:
                        #random_enemy = get_obj_display('units').unit_list[enemy_country][enemy_list[random.randint(0, len(enemy_list)-1)]][0]
                        random_enemy = get_obj_display('units').unit_list[enemy_country][enemy_list[0]][0]
                        random_enemy.health -= self.damage

                        shoot_sound.play('hit.wav')

                        if random_enemy.health <= 0:
                            if random_enemy.type == 4:
                                shoot_sound.play('explosion.wav')

                            if self.flip == 0:
                                get_obj_display('game_rule').money += get_obj_display('game_rule').money_kill_unit[random_enemy.type]

                                if self.flip == 0:
                                    get_obj_display('game_info').info['kills'] += 1
                                else:
                                    get_obj_display('game_info').info['death'] += 1

                else:
                    get_obj_display('dot').dot_list[0 if (self.flip == 1) else 1][2] -= self.damage

                    shoot_sound.play('hit.wav')

                    if get_obj_display('dot').dot_list[0 if (self.flip == 1) else 1][2] <= 0:
                        get_obj_display('game_rule')._end_game()

                self.time_shoot = time.perf_counter() + self.delay_shoot

        if self.type == 4:
            if self.health <= 0:
                self.state = 4

            elif self.health < self.state_health * (3 - self.state):
                self.state += 1

        else:
            self.state += 0.15
            if self.state >= 8:
                self.state = 0

    def draw(self, x, y):
        self.images[int(self.state)].x = self.pos_x + x
        self.images[int(self.state)].y = y + self.pos_y - (0 if (self.type == 4 ) else (self.images[int(self.state)].height / 6))
        drawp(self.images[int(self.state)])

        if settings.game_options['game_unit_info'] and get_obj_other('setings_game').draw_gui and not get_obj_display('world').menu:
            self.unit_text.label.x = self.pos_x + x + self.images[int(self.state)].width / 2
            self.unit_text.label.y = y + self.pos_y + self.images[int(self.state)].height + settings.height / 50
            drawp(self.unit_text)

        if settings.game_options['game_shadows']:
            self.images_shadows[int(self.state)].x = self.pos_x + x
            self.images_shadows[int(self.state)].y = y - self.images_shadows[int(self.state)].height + self.pos_y + (0 if (self.type == 4 ) else (self.images[int(self.state)].height / 6))
            drawp(self.images_shadows[int(self.state)])
