class clouds():
    def __init__(self):
        self.image = image_label('world/clouds/cloud.png', 100 , settings.height - 100, scale=settings.height/240, alpha=155)

    def update(self):
        pass

    def draw(self):
        drawp(self.image)
