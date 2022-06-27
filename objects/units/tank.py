
class tank():
    def __init__(self, x, y, images, images_shadows, type=0, flip=0):
        self.type = type
        self.flip = flip

        self.health = 100
        self.damage = 10

        self.images = images
        self.images_shadows = images_shadows

        self.stop = False

        self.pos_x = (-self.images[0].width + x) if (flip == 0) else (get_obj_display('world').image.sprite.width + x)
        self.pos_y = y
        self.speed = self.images[0].width/400
        if flip:
            self.speed = -self.speed

        self.state = 0

    def update(self):

        if not self.stop:
            self.pos_x += self.speed

            if (
                ((self.pos_x > get_obj_display('world').image.sprite.width - (self.images[0].width * 2)) and self.flip == 0) or
                (self.pos_x < (self.images[0].width)) and self.flip == 1):
                self.stop = True

    def draw(self, x, y):
        self.images[self.state].x = self.pos_x + x
        self.images[self.state].y = y + self.pos_y
        drawp(self.images[self.state])

        if settings.game_options['game_shadows']:
            self.images_shadows[self.state].x = self.pos_x + x
            self.images_shadows[self.state].y = y - self.images_shadows[self.state].height + self.pos_y
            drawp(self.images_shadows[self.state])
