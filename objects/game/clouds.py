class clouds():
    def __init__(self):
        self.image = image_label('world/clouds/cloud.png', 100 , settings.height - 100, scale=SCALE_WORLD, alpha=50)

    def update(self):
        pass

    def draw(self):
        drawp(self.image)
