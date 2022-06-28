class rope():
    def __init__(self):
        self.pos = [0, get_obj_display('world').image_width]
        self.rope_pos = get_obj_display('world').image_width / 2

        self.speed = 0

    def update(self):
        self.speed = 1
        tank_buf = None
        self.state = [False, False]

        for i in range(2):
            for tank in get_obj_display('units').tank_list[i]:
                if tank[0].stopline_bool and tank[0].health > 0:
                    self.state[i] = True
                    if tank[0].speed > self.speed:
                        self.speed = tank[0].speed
                        tank_buf = tank[0]

        self.tick_speed = self.speed / get_obj_display('world').pixel_size

        if self.state[0] and not self.state[1]:
            tank_buf.stop = False
            tank_buf.stopline_bool = False
            self.rope_pos += self.tick_speed
        elif not self.state[0] and self.state[1]:
            tank_buf.stop = False
            tank_buf.stopline_bool = False
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
