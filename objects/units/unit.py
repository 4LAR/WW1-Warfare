
class unit():
    def __init__(self, x, y, images, images_shadows, type=0, flip=0):

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

        if type == 0:
            self.health = 100
            self.damage = 50
            self.delay_shoot = 1
            self.speed = settings.width/1500

        elif type == 1:
            self.health = 100
            self.damage = 25
            self.delay_shoot = 1
            self.speed = settings.width/1500

        elif type == 2:
            self.health = 100
            self.damage = 100
            self.delay_shoot = 1
            self.speed = settings.width/1500

        elif type == 3:
            self.health = 100
            self.damage = 200
            self.delay_shoot = 1
            self.speed = settings.width/1500

        elif type == 4:
            self.health = 1000
            self.damage = 200
            self.delay_shoot = 0.5
            self.speed = self.images[0].width/400

        self.stopline_bool = False

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

        if not self.stop and self.health > 0:
            self.pos_x += self.speed

            #if (
            #    ((self.pos_x > get_obj_display('world').image.sprite.width - (self.images[0].width * 2)) and self.flip == 0) or
            #    (self.pos_x < (self.images[0].width)) and self.flip == 1):
            #    self.stop = True

        if (((self.pos_x + self.images[0].width + self.images[0].width/2 > get_obj_display('world').pos_with_world(get_obj_display('rope').rope_pos)) and self.flip == 0) or
            ((self.pos_x - self.images[0].width/2 < get_obj_display('world').pos_with_world(get_obj_display('rope').rope_pos)) and self.flip == 1)):

            self.stop = True
            self.stopline_bool = True

        else:
            self.stop = False
            self.stopline_bool = False

        if self.time_shoot <= time.perf_counter():
            enemy_list = []
            enemy_country = 1 if (self.flip == 0) else 0
            if self.health > 0 and self.stopline_bool and len(get_obj_display('units').unit_list[enemy_country]) > 0: #and get_obj_display('rope').state == [True, True]:
                for i in range(len(get_obj_display('units').unit_list[enemy_country])):
                    if get_obj_display('units').unit_list[enemy_country][i][0].health > 0 and get_obj_display('units').unit_list[enemy_country][i][0].stopline_bool:
                        enemy_list.append(i)

                if len(enemy_list) > 0:
                    random_enemy = get_obj_display('units').unit_list[enemy_country][enemy_list[random.randint(0, len(enemy_list)-1)]][0]
                    random_enemy.health -= self.damage

                    if random_enemy.health <= 0 and self.flip == 0:
                        get_obj_display('game_rule').money += get_obj_display('game_rule').money_kill_unit[random_enemy.type]

                self.time_shoot = time.perf_counter() + self.delay_shoot

        if self.type == 4:
            if self.health <= 0:
                self.state = 4

            elif self.health < self.state_health * (3 - self.state):
                self.state += 1

    def draw(self, x, y):
        self.images[self.state].x = self.pos_x + x
        self.images[self.state].y = y + self.pos_y
        drawp(self.images[self.state])

        if settings.game_options['game_shadows']:
            self.images_shadows[self.state].x = self.pos_x + x
            self.images_shadows[self.state].y = y - self.images_shadows[self.state].height + self.pos_y
            drawp(self.images_shadows[self.state])
