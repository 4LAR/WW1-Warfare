class vegetation():
    def __init__(self):

        self.tree_list = []
        self.images = [
            [image_label('world/vegetation/tree.png', 0 , 0, scale=SCALE_WORLD), settings.height/2.7, 0],
            [image_label('world/vegetation/tree_1.png', 0 , 0, scale=SCALE_WORLD), settings.height/2.7, 0],
            [image_label('world/vegetation/tree_2.png', 0 , 0, scale=SCALE_WORLD), settings.height/2.7, 0],
            [image_label('world/vegetation/tree_3.png', 0 , 0, scale=SCALE_WORLD), settings.height/3.9, -settings.height/8],
            [image_label('world/vegetation/tree_4.png', 0 , 0, scale=SCALE_WORLD), settings.height/2.7, 0],
            [image_label('world/vegetation/tree_5.png', 0 , 0, scale=SCALE_WORLD), settings.height/2.7, 0],
            [image_label('world/vegetation/tree_6.png', 0 , 0, scale=SCALE_WORLD), settings.height/2.7, 0],
            [image_label('world/vegetation/tree_7.png', 0 , 0, scale=SCALE_WORLD), settings.height/2.7, 0],
            [image_label('world/vegetation/tree_8.png', 0 , 0, scale=SCALE_WORLD), settings.height/2.7, 0],
            [image_label('world/vegetation/tree_9.png', 0 , 0, scale=SCALE_WORLD), settings.height/2.7, 0]
        ]

        self.image_shadows = []
        for image in self.images:
            self.image_shadows.append(
                PIL_to_pyglet(image_transform_for_shadow('assets/img/%s' % image[0].image_name, SHADOWS_COLOR), SCALE_WORLD)
            )

        #self.tree_list.append([type, position_x, position_y(up-0, down-1)])
        self.load()

    def load(self):
        self.tree_list = []
        for el in get_obj_display('world_save').dict['world']['vegetation']:
            self.tree_list.append(el)

    def update(self):
        pass

    def draw(self, pos_y=0, shadows=False, only_shadows=False):
        for tree in self.tree_list:
            if tree[2] == pos_y:
                x = get_obj_display('world').pos_with_world(tree[1]) + get_obj_display('world').move_x + get_obj_display('world').map_offs[0] * (1.2 if (tree[2] == 1) else 1)
                y = get_obj_display('world').map_offs[1] - get_obj_display('world').fov/2 + self.images[tree[0]][tree[2] + 1]

                if not only_shadows:
                    self.images[tree[0]][0].sprite.x = x
                    self.images[tree[0]][0].sprite.y = y
                    drawp(self.images[tree[0]][0])

                if sattings_game.shadows and shadows:
                    self.image_shadows[tree[0]].x = x - (self.image_shadows[tree[0]].width/20 if (tree[0] == 3) else 0)# + (self.image_shadows[tree[0]].width/8 if (tree[0] != 2) else self.image_shadows[tree[0]].width/50)
                    self.image_shadows[tree[0]].y = y - (self.image_shadows[tree[0]].height/20 if (tree[0] == 3) else self.image_shadows[tree[0]].height)# - (self.image_shadows[tree[0]].height/1.4 if (tree[0] != 2) else self.image_shadows[tree[0]].height/4)
                    drawp(self.image_shadows[tree[0]])


class vegetation_up_shadows():
    def draw(self):
        get_obj_display('vegetation').draw(0, True, True)

class vegetation_down():
    def draw(self):
        get_obj_display('vegetation').draw(1, True)
