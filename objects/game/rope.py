class rope():
    def __init__(self):
        self.pos = [0, get_obj_display('world').image_width]
        self.rope_pos = get_obj_display('world').image_width / 2

    def update(self):
        pass

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
