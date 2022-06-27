#SCALE = settings.height / 120

class human_():

    def get_pos_by_deg(self, deg, size):
        #deg += 90
        if deg < 0:
            deg = 180 + (180 + deg)
        if deg >= 360:
            deg = 0
        a = size/math.sin(math.radians(90))
        x = a * math.sin(math.radians(deg))
        y = a * math.sin(math.radians(180 - 90 - deg))
        return x, y

    def add_bone(self, image, bone=None, deg=0, height=1, anchor_x=1, anchor_y=1, rotation=0, nopos_bool=False, mask=False):

        if mask:
            image_buf = Image.open('assets/img/%s' % image)
            image_ = Image.new('RGBA', (image_buf.width, image_buf.height))

            image_shadow = get_pil_black_mask(image_buf.copy(), self.shadow_alpha)
            image_mask = get_pil_black_mask(image_buf.copy(), 256)
            image_buf.paste(image_mask, (0, 0), image_shadow)

            raw_image = image_buf.tobytes()
            image_buf = pyglet.image.ImageData(image_buf.width, image_buf.height, 'RGBA', raw_image, pitch=-image_buf.width * 4)

        else:
            image_buf = pyglet.image.load('assets/img/%s' % image)

        image_buf.anchor_x = int(image_buf.width // anchor_x)
        image_buf.anchor_y = int(image_buf.height // anchor_y)

        if bone != None:
            x, y = self.get_pos_by_deg(bone[0].rotation + deg, bone[0].height * height)
            image_buf = pyglet.sprite.Sprite(image_buf, x = (self.pos_x if not nopos_bool else bone[0].x) + x, y = bone[0].y + y, batch=self.batch)
        else:
            image_buf = pyglet.sprite.Sprite(image_buf, x = self.pos_x, y = self.pos_y, batch=self.batch)

        image_buf.scale = SCALE_WORLD/1.2

        tex = image_buf.image.get_texture()

        glTexParameteri(tex.target, GL_TEXTURE_MIN_FILTER, GL_NEAREST)
        glTexParameteri(tex.target, GL_TEXTURE_MAG_FILTER, GL_NEAREST)

        image_buf.rotation = rotation

        return [image_buf, deg, height, nopos_bool, rotation]

    def update_bone(self, bone, mother_bone=None, rotation=None):

        if mother_bone != None:
            x, y = self.get_pos_by_deg(mother_bone[0].rotation + bone[1], mother_bone[0].height * bone[2])
            bone[0].x = (self.pos_x if not bone[3] else mother_bone[0].x) + x
            bone[0].y = mother_bone[0].y + y

        else:
            bone[0].x = self.pos_x
            bone[0].y = self.pos_y

        if rotation != None:
            bone[0].rotation = rotation
            bone[4] = rotation
        else:
            bone[0].rotation = bone[4]

        return bone

    def update_pos(self, x, y):
        self.pos_x = x
        self.pos_y = y

    def __init__(self, x, y, country='germany', type_body=1, type_head=1, type_hand=1, type_leg=1, type_weapon=1):

        self.batch_bool = False

        self.shadow_alpha = 45

        self.pos_x = x#settings.width/2
        self.pos_y = y#settings.height/2

        self.batch = pyglet.graphics.Batch()

        self.body = self.add_bone('world/units/human/%s/body/%d.png' % (country, type_body), anchor_x=2, anchor_y=2, rotation=4)
        self.head = self.add_bone('world/units/human/%s/head/%d.png' % (country, type_head), bone=self.body, deg=4, height=1.02, anchor_x=2, anchor_y=1, nopos_bool=True)

        #self.R_leg = self.add_bone('human/leg_1.png', bone=self.body, deg=-20, height=(1/-2.8), anchor_x=2, anchor_y=1, rotation=-20, nopos_bool=True, mask=True)
        self.R_leg = self.add_bone('world/units/human/%s/leg/%d/leg_1.png' % (country, type_leg), bone=self.body, deg=-20, height=(1/-2.5), anchor_x=2, anchor_y=1, rotation=-20, nopos_bool=True, mask=True)
        self.R_leg_1 = self.add_bone('world/units/human/%s/leg/%d/leg_2.png' % (country, type_leg), bone=self.R_leg, deg=-10, height=(1/-1.4), anchor_x=2, anchor_y=1, rotation=10, nopos_bool=True, mask=True)
        self.R_leg_2 = self.add_bone('world/units/human/%s/leg/%d/leg_3.png' % (country, type_leg), bone=self.R_leg_1, deg=-10, height=-1, anchor_x=1.5, anchor_y=1, rotation=0, nopos_bool=True, mask=True)

        #self.L_leg = self.add_bone('human/leg_1.png', bone=self.body, deg=20, height=(1/-2.8), anchor_x=2, anchor_y=1, rotation=-20, nopos_bool=True)
        self.L_leg = self.add_bone('world/units/human/%s/leg/%d/leg_1.png' % (country, type_leg), bone=self.body, deg=20, height=(1/-2.5), anchor_x=2, anchor_y=1, rotation=-20, nopos_bool=True)
        self.L_leg_1 = self.add_bone('world/units/human/%s/leg/%d/leg_2.png' % (country, type_leg), bone=self.L_leg, deg=-10, height=(1/-1.4), anchor_x=2, anchor_y=1, rotation=10, nopos_bool=True)
        self.L_leg_2 = self.add_bone('world/units/human/%s/leg/%d/leg_3.png' % (country, type_leg), bone=self.L_leg_1, deg=-10, height=-1, anchor_x=1.5, anchor_y=1, rotation=0, nopos_bool=True)

        self.R_hand = self.add_bone('world/units/human/%s/hand/%d/hand_1.png' % (country, type_hand), bone=self.body, deg=-145, height=(1/-2), anchor_x=2, anchor_y=1, rotation=-20, nopos_bool=True, mask=True)
        self.R_hand_1 = self.add_bone('world/units/human/%s/hand/%d/hand_2.png' % (country, type_hand), bone=self.R_hand, deg=0, height=(1/-1.1), anchor_x=2, anchor_y=1, rotation=-20, nopos_bool=True, mask=True)
        self.R_hand_2 = self.add_bone('world/units/human/%s/hand/%d/hand_3.png' % (country, type_hand), bone=self.R_hand_1, deg=0, height=(1/-1.1), anchor_x=2, anchor_y=1, rotation=-40, nopos_bool=True, mask=True)
        self.R_hand_3 = self.add_bone('world/units/human/%s/hand/%d/hand_4.png' % (country, type_hand), bone=self.R_hand_2, deg=0, height=(1/-1.1), anchor_x=2, anchor_y=1, rotation=-90, nopos_bool=True, mask=True)

        self.L_hand = self.add_bone('world/units/human/%s/hand/%d/hand_1.png' % (country, type_hand), bone=self.body, deg=145, height=(1/-2), anchor_x=2, anchor_y=1, rotation=20, nopos_bool=True)
        self.L_hand_1 = self.add_bone('world/units/human/%s/hand/%d/hand_2.png' % (country, type_hand), bone=self.L_hand, deg=0, height=(1/-1.1), anchor_x=2, anchor_y=1, rotation=-20, nopos_bool=True)
        self.L_hand_2 = self.add_bone('world/units/human/%s/hand/%d/hand_3.png' % (country, type_hand), bone=self.L_hand_1, deg=0, height=(1/-1.1), anchor_x=2, anchor_y=1, rotation=-40, nopos_bool=True)
        self.L_hand_3 = self.add_bone('world/units/human/%s/hand/%d/hand_4.png' % (country, type_hand), bone=self.L_hand_2, deg=0, height=(1/-1.1), anchor_x=2, anchor_y=1, rotation=-90, nopos_bool=True)

        self.weapon = self.add_bone('world/units/human/%s/weapons/%d.png' % (country, type_weapon), bone=self.L_hand_3, deg=0, height=(1/-1.1), anchor_x=2, anchor_y=1.4, rotation=-90, nopos_bool=True)

        self.anim_play('walk')

        self.anim_state = 0
        self.anim_end = False

        self.delay = 0.2#0.20
        self.time = time.perf_counter() + self.delay

        self.last_anim = [
            0, 0,

            0, 0, 0,
            0, 0, 0,

            0, 0, 0, 0,
            0, 0, 0, 0,

            0,

            0
        ]

    def anim_play(self, name):
        self.anim = read_dict('assets/anim/%s' % name)
        self.anim_end = False
        self.anim_state = 0

    def on_key_press(self, symbol, modifiers):
        if symbol == key.F8:
            self.anim_play('shoot')

        if symbol == key.F10:
            self.anim_play('run')

        if symbol == key.F11:
            self.anim_play('walk')

        if symbol == key.F12:
            self.anim_play('death')

        if symbol == key.F6:
            self.anim_play('aiming_1')

        if symbol == key.F7:
            self.anim_play('aiming_2')

    async def update(self):
        if not self.anim_end:
            if self.time <= time.perf_counter():
                self.last_anim = self.anim['list'][self.anim_state]
                self.anim_state += 1
                if self.anim_state >= len(self.anim['list']):

                    if self.anim['info']['loop']:
                        self.anim_state = 0

                    else:
                        self.anim_state = len(self.anim)-1
                        self.anim_end = True

                self.delay = self.anim['list'][self.anim_state][17]

                self.time = time.perf_counter() + self.delay

            anim = self.anim['list'][self.anim_state]

            old_anim = self.last_anim

            time_p = (1 - (self.time - time.perf_counter())*(1/self.delay))

            self.body = self.update_bone(self.body, rotation=lerp(old_anim[0], anim[0], time_p))

            self.head = self.update_bone(self.head, self.body, rotation=lerp(old_anim[1], anim[1], time_p))

            self.R_leg = self.update_bone(self.R_leg, self.body, rotation=lerp(old_anim[2], anim[2], time_p))
            self.R_leg_1 = self.update_bone(self.R_leg_1, self.R_leg, rotation=lerp(old_anim[3], anim[3], time_p))
            self.R_leg_2 = self.update_bone(self.R_leg_2, self.R_leg_1, rotation=lerp(old_anim[4], anim[4], time_p))

            self.L_leg = self.update_bone(self.L_leg, self.body, rotation=lerp(old_anim[5], anim[5], time_p))
            self.L_leg_1 = self.update_bone(self.L_leg_1, self.L_leg, rotation=lerp(old_anim[6], anim[6], time_p))
            self.L_leg_2 = self.update_bone(self.L_leg_2, self.L_leg_1, rotation=lerp(old_anim[7], anim[7], time_p))

            self.R_hand = self.update_bone(self.R_hand, self.body, rotation=lerp(old_anim[8], anim[8], time_p))
            self.R_hand_1 = self.update_bone(self.R_hand_1, self.R_hand, rotation=lerp(old_anim[9], anim[9], time_p))
            self.R_hand_2 = self.update_bone(self.R_hand_2, self.R_hand_1, rotation=lerp(old_anim[10], anim[10], time_p))
            self.R_hand_3 = self.update_bone(self.R_hand_3, self.R_hand_2, rotation=lerp(old_anim[11], anim[11], time_p))

            self.L_hand = self.update_bone(self.L_hand, self.body, rotation=lerp(old_anim[12], anim[12], time_p))
            self.L_hand_1 = self.update_bone(self.L_hand_1, self.L_hand, rotation=lerp(old_anim[13], anim[13], time_p))
            self.L_hand_2 = self.update_bone(self.L_hand_2, self.L_hand_1, rotation=lerp(old_anim[14], anim[14], time_p))
            self.L_hand_3 = self.update_bone(self.L_hand_3, self.L_hand_2, rotation=lerp(old_anim[15], anim[15], time_p))

            self.update_bone(self.weapon, self.L_hand_3, rotation=lerp(old_anim[16], anim[16], time_p))

    def draw(self):
        if not self.batch_bool:
            drawp(self.R_leg_1[0])
            drawp(self.R_leg_2[0])
            drawp(self.R_leg[0])

            drawp(self.L_leg_1[0])
            drawp(self.L_leg_2[0])
            drawp(self.L_leg[0])

            drawp(self.R_hand_2[0])
            drawp(self.R_hand_1[0])
            drawp(self.R_hand_3[0])
            drawp(self.R_hand[0])

            drawp(self.body[0])
            drawp(self.head[0])

            drawp(self.weapon[0])
            drawp(self.L_hand_2[0])
            drawp(self.L_hand_1[0])
            drawp(self.L_hand_3[0])
            drawp(self.L_hand[0])

        else:
            self.batch.draw()

def menu_():
    clear_display()
    add_display(human())

    # Вывод горячих клавиш в консоль
    console_term.print("-"*20)
    console_term.print("HOTKEYS")
    console_term.print("F6 - Убрать прицеливание")
    console_term.print("F7 - Прицеливание")
    console_term.print("F8 - Выстрел")
    console_term.print("")
    console_term.print("F10 - Бег")
    console_term.print("F11 - Идти")
    console_term.print("F12 - Смэрть")
    console_term.print("-"*20)
