class game_rule():
    def __init__(self):
        self.pause = False
        self.pause_settings = False
        self.play_fast = False

        self.tank_speed = SCALE_WORLD / 10

    def _pause_settings(self):
        self.pause_settings = True
        self.pause = True

    def _unpause_settings(self):
        self.pause_settings = False
        self.pause = False

    def _play(self):
        self.pause = False
        self.play_fast = False

    def _pause(self):
        self.pause = True
        self.play_fast = False

    def _play_fast(self):
        self.pause = False
        self.play_fast = True

    #def update(self):
    #    print(self.pause)
    #    print(self.pause_settings)
    #    print(self.play_fast)
    #    print('-'*10)
