class rope():
    def __init__(self):
        self.pos = [0, get_obj_display('world').image_width]
        self.rope_pos = get_obj_display('world').image_width / 2

        self.speed = 0

    def update(self):
        if not get_obj_display('game_rule').pause:
            self.speed = 0
            tank_buf = [None, None]
            self.state = [False, False]

            for i in range(2):
                for tank in get_obj_display('units').unit_list[i]:
                    if tank[0].stopline_bool and tank[0].health > 0:
                        self.state[i] = True
                        if abs(tank[0].speed) > self.speed:
                            self.speed = abs(tank[0].speed)
                            tank_buf[i] = tank[0]

            self.tick_speed = self.speed / get_obj_display('world').pixel_size

            if self.state[0] and not self.state[1]:
                tank_buf[0].stop = False
                self.rope_pos += self.tick_speed
                
            elif not self.state[0] and self.state[1]:
                tank_buf[1].stop = False
                self.rope_pos -= self.tick_speed

    def draw(self):
        if settings.game_options['draw_rope']:
            x = get_obj_display('world').move_x + get_obj_display('world').map_offs[0]
            y = get_obj_display('world').map_offs[1] - get_obj_display('world').fov/2 + (settings.height/2.7)/2

            pos_x = x + get_obj_display('world').pos_with_world(self.rope_pos)
            draw_line(
                (int(pos_x), 0),
                (int(pos_x), settings.height)
            )

            for pos in self.pos:
                pos_x = x + get_obj_display('world').pos_with_world(pos)
                draw_line(
                    (int(pos_x), 0),
                    (int(pos_x), settings.height)
                )
