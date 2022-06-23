
class tank():
    def __init__(self, type=0, flip=0):
        self.type = type
        self.flip = flip

        self.health = 100
        self.damage = 10

        self.images = []
        self.images_shadows = []

        self.stop = False

        tanks_types = [
            ['mark-1', 5],
            ['a7v', 5]
        ]

        for i in range(tanks_types[type][1]):
            self.images.append(Image.open('assets/img/world/units/%s/%d.png' % (tanks_types[type][0], i + 1)))
            if flip == 0:
                self.images[i] = self.images[i].transpose(Image.FLIP_LEFT_RIGHT)

            self.images_shadows.append(PIL_to_pyglet(image_transform_for_shadow(self.images[i], SHADOWS_COLOR, True), SCALE_WORLD/1.2))

            self.images[i] = PIL_to_pyglet(self.images[i], SCALE_WORLD/1.2)

        self.pos_x = -self.images[0].width if (flip == 0) else (get_obj_display('world').image.sprite.width)
        self.speed = self.images[0].width/400
        if flip:
            self.speed = -self.speed

        self.state = 0

    async def update(self):

        if not self.stop:
            self.pos_x += self.speed

            if (
                ((self.pos_x > get_obj_display('world').image.sprite.width - (self.images[0].width * 2)) and self.flip == 0) or
                (self.pos_x < (self.images[0].width)) and self.flip == 1):
                self.stop = True

    def draw(self, x, y):
        self.images[self.state].x = self.pos_x + x
        self.images[self.state].y = y
        drawp(self.images[self.state])

        self.images_shadows[self.state].x = self.pos_x + x
        self.images_shadows[self.state].y = y - self.images_shadows[self.state].height
        drawp(self.images_shadows[self.state])
