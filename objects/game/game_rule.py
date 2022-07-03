class game_rule():
    def __init__(self):
        self.pause = False
        self.pause_settings = False
        self.play_fast = False
        self.end_game = False

        self.tank_speed = SCALE_WORLD / 10

        self.money = int(get_obj_display('world_save').dict['info']['money'])
        self.money_tick = 1
        self.money_delay = 1
        self.money_kill_unit = {
            0: 10,
            1: 15,
            2: 15,
            3: 15,
            4: 100
        }
        self.money_time = time.perf_counter() + self.money_delay

    def _end_game(self):
        self.end_game = True
        self.pause = True

        off_input()
        add_display(timer(5, arg="add_display(breathing_label(0, 0, settings.width, settings.height, (0, 0, 0), 0, delay=0.01, for_from=0, for_before=255, tick=2.5, arg='menu()'))"))


    def _pause_settings(self):
        if not self.end_game:
            self.pause_settings = True
            self.pause = True

    def _unpause_settings(self):
        if not self.end_game:
            self.pause_settings = False
            self.pause = False

    def _play(self):
        if not self.end_game:
            self.pause = False
            self.play_fast = False

    def _pause(self):
        if not self.end_game:
            self.pause = True
            self.play_fast = False

    def _play_fast(self):
        if not self.end_game:
            self.pause = False
            self.play_fast = True

    def update(self):
        if not self.pause:
            if self.money_time <= time.perf_counter():
                self.money += self.money_tick

                self.money_time = time.perf_counter() + self.money_delay

    #def update(self):
    #    print(self.pause)
    #    print(self.pause_settings)
    #    print(self.play_fast)
    #    print('-'*10)
