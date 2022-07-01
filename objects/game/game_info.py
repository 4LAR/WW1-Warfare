class game_info():
    def __init__(self):
        self.info = {
            'kills': 0,
            'death': 0,
            'unit_spawned': 0,
            'enemy_unit_spawned': 0,
            'time': '',
            'money_spent': 0
        }

    def update_(self):
        print(self.info)
