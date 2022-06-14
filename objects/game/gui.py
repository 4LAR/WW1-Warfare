class gui():
    def __init__(self):

        buttons_distance = settings.width/25
        self.settings_button = image_button(
            settings.width/100, settings.height - settings.height/12,
            image = 'buttons/gui/settings.png',
            image_selected = 'buttons/gui/settings.png',
            scale = settings.height/150
        )

        self.play_fast_button = image_button(
            settings.width/100 + buttons_distance, settings.height - settings.height/12,
            image = 'buttons/gui/play_fast.png',
            image_selected = 'buttons/gui/play_fast.png',
            scale = settings.height/150
        )

        self.play_button = image_button(
            settings.width/100 + (buttons_distance)*2, settings.height - settings.height/12,
            image = 'buttons/gui/play.png',
            image_selected = 'buttons/gui/play.png',
            scale = settings.height/150
        )

        self.pause_button = image_button(
            settings.width/100 + (buttons_distance)*3, settings.height - settings.height/12,
            image = 'buttons/gui/pause.png',
            image_selected = 'buttons/gui/pause.png',
            scale = settings.height/150
        )

    def draw(self):
        drawp(self.settings_button)
        drawp(self.play_fast_button)
        drawp(self.play_button)
        drawp(self.pause_button)
