def load_units_info(self):
    self.units_info = {
        "rus": [],
        "britain": [
            {
                "name": "infantry",
                "ico": "infantry",
                "image": "",
                "id": 0,
                "money": 10,
                "tick": 0.5,
                "count_tick": 100,

                "health": 100,
                "demage": 50,
                "delay_shoot": 1,
                "speed": 1500,

                "priority": [1, 0, 3, 2, 4]
            },{
                "name": "machine gunner",
                "ico": "human_with_mask",
                "image": "",
                "id": 1,
                "money": 15,
                "tick": 0.5,
                "count_tick": 200,

                "health": 200,
                "demage": 25,
                "delay_shoot": 0.5,
                "speed": 1500,

                "priority": [1, 0, 3, 2, 4]
            },{
                "name": "sniper",
                "ico": "none",
                "image": "",
                "id": 2,
                "money": 15,
                "tick": 0.5,
                "count_tick": 200,

                "health": 100,
                "demage": 100,
                "delay_shoot": 1.5,
                "speed": 1500,

                "priority": [1, 0, 3, 2, 4]
            },{
                "name": "mortar man",
                "ico": "none",
                "image": "",
                "id": 3,
                "money": 15,
                "tick": 0.5,
                "count_tick": 200,

                "health": 100,
                "demage": 200,
                "delay_shoot": 2,
                "speed": 1500,

                "priority": [4, 1, 0, 3, 2]
            },{
                "name": "tank",
                "ico": "tank",
                "image": "mark-1",
                "id": 4,
                "money": 100,
                "tick": 0.5,
                "count_tick": 1000,

                "health": 1000,
                "demage": 200,
                "delay_shoot": 2,
                "speed": 1500,

                "priority": [4, 1, 0, 3, 2]
            },{
                "name": "bomb",
                "ico": "none",
                "image": "",
                "id": 5,
                "money": 100,
                "tick": 0.5,
                "count_tick": 1500,

                "demage": 1000
            },{
                "name": "gas bomb",
                "ico": "none",
                "image": "",
                "id": 6,
                "money": 150,
                "tick": 0.5,
                "count_tick": 2000,

                "demage": 100,
                "delay_shoot": 0.2
            }
        ],
        "france": [],
        "germany": [
            {
                "name": "infantry",
                "ico": "infantry",
                "image": "",
                "id": 0,
                "money": 10,
                "tick": 0.5,
                "count_tick": 100,

                "health": 100,
                "demage": 50,
                "delay_shoot": 1,
                "speed": 1500,

                "priority": [1, 0, 3, 2, 4]
            },{
                "name": "machine gunner",
                "ico": "machine_gunner",
                "image": "",
                "id": 1,
                "money": 15,
                "tick": 0.5,
                "count_tick": 200,

                "health": 200,
                "demage": 25,
                "delay_shoot": 0.5,
                "speed": 1500,

                "priority": [1, 0, 3, 2, 4]
            },{
                "name": "sniper",
                "ico": "sniper",
                "image": "",
                "id": 2,
                "money": 15,
                "tick": 0.5,
                "count_tick": 200,

                "health": 100,
                "demage": 100,
                "delay_shoot": 1.5,
                "speed": 1500,

                "priority": [1, 0, 3, 2, 4]
            },{
                "name": "mortar man",
                "ico": "none",
                "image": "",
                "id": 3,
                "money": 15,
                "tick": 0.5,
                "count_tick": 200,

                "health": 100,
                "demage": 200,
                "delay_shoot": 2,
                "speed": 1500,

                "priority": [4, 1, 0, 3, 2]
            },{
                "name": "tank",
                "ico": "tank",
                "image": "a7v",
                "id": 4,
                "money": 100,
                "tick": 0.5,
                "count_tick": 1000,

                "health": 1000,
                "demage": 200,
                "delay_shoot": 2,
                "speed": 1500,

                "priority": [4, 1, 0, 3, 2]
            },{
                "name": "bomb",
                "ico": "bomb_1",
                "image": "",
                "id": 5,
                "money": 100,
                "tick": 0.5,
                "count_tick": 1500,

                "demage": 1000
            },{
                "name": "gas bomb",
                "ico": "bomb",
                "image": "",
                "id": 6,
                "money": 150,
                "tick": 0.5,
                "count_tick": 2000,

                "demage": 100,
                "delay_shoot": 0.2
            }
        ]
    }

    json.dump(self.units_info, open(self.path, 'w'), indent=4)
