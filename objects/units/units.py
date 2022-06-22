class units():
    def __init__(self):
        self.human_speed = SCALE_WORLD/2

        self.human_list = []
        self.tank_list = []

        #self.humans.append([human(0, 0), 0])

    def add_unit(self, type=0):
        y = random.randint(-settings.height/10, settings.height/10)
        if type == 0:
            self.human_list.append([human(0, 0), 0, y, False])

        elif type == 1:
            self.human_list.append([human(0, 0, 'germany', 1, 2, 1, 1, 2), 0, y, False])

        elif type == 2:
            self.tank_list.append(tank(1))

    def draw(self):
        x = get_obj_display('world').move_x + get_obj_display('world').map_offs[0]
        y = get_obj_display('world').map_offs[1] - get_obj_display('world').fov/2 + (settings.height/2.7)/2

        for tank in self.tank_list:
            if not get_obj_display('game_rule').pause:
                threading.Thread(target=tank.update).start()
                #tank.update()
            tank.draw(x, y)

        for human in self.human_list:
            if not get_obj_display('game_rule').pause:
                if not human[3]:
                    human[1] += self.human_speed
                    if (x + human[1] > get_obj_display('world').image.sprite.width):
                        human[3] = True
                    human[0].update_pos(x + human[1], y + human[2])
                threading.Thread(target=human[0].update).start()
                #multiprocessing.Process(target=human[0].update).start()
                #human[0].update()
            human[0].draw()
