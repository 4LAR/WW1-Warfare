class vegetation():
    def __init__(self):

        self.tree_list = []
        self.images = [
            [image_label('world/vegetation/tree.png', 0 , 0, scale=SCALE_WORLD), settings.height/2.7, 0],
            [image_label('world/vegetation/tree_1.png', 0 , 0, scale=SCALE_WORLD), settings.height/2.7, 0],
            [image_label('world/vegetation/tree_2.png', 0 , 0, scale=SCALE_WORLD), settings.height/3.9, -settings.height/8],
            [image_label('world/vegetation/tree_3.png', 0 , 0, scale=SCALE_WORLD), settings.height/2.7, 0]
        ]



        self.image_shadows = [
            #PIL_to_pyglet(get_pil_color_mask(Image.open('assets/img/world/vegetation/tree.png').transpose(Image.FLIP_LEFT_RIGHT).rotate(shadows_deg, PIL.Image.NEAREST, expand = 1), shadows_color), SCALE_WORLD),
            PIL_to_pyglet(image_transform_for_shadow('assets/img/world/vegetation/tree.png', SHADOWS_COLOR), SCALE_WORLD),
            PIL_to_pyglet(image_transform_for_shadow('assets/img/world/vegetation/tree_1.png', SHADOWS_COLOR), SCALE_WORLD),
            PIL_to_pyglet(image_transform_for_shadow('assets/img/world/vegetation/tree_2.png', SHADOWS_COLOR), SCALE_WORLD),
            PIL_to_pyglet(image_transform_for_shadow('assets/img/world/vegetation/tree_3.png', SHADOWS_COLOR), SCALE_WORLD)
        ]

        self.tree_list.append([0, 4, 0])
        self.tree_list.append([3, 30, 0])
        self.tree_list.append([0, 50, 0])
        self.tree_list.append([1, 100, 0])
        self.tree_list.append([2, 150, 0])

        #self.tree_list.append([0, 5, 1])
        self.tree_list.append([0, 30, 1])
        self.tree_list.append([3, 60, 1])

        self.tree_list.append([1, 150, 1])
        self.tree_list.append([2, 200, 1])

    def update(self):
        pass

    def draw(self):
        for tree in self.tree_list:
            x = get_obj_display('world').pos_with_world(tree[1]) + get_obj_display('world').move_x + get_obj_display('world').map_offs[0] * (1.2 if (tree[2] == 1) else 1)
            y = get_obj_display('world').map_offs[1] - get_obj_display('world').fov/2 + self.images[tree[0]][tree[2] + 1]

            self.images[tree[0]][0].sprite.x = x
            self.images[tree[0]][0].sprite.y = y
            drawp(self.images[tree[0]][0])

            if sattings_game.shadows:
                self.image_shadows[tree[0]].x = x - (self.image_shadows[tree[0]].width/20 if (tree[0] == 2) else 0)# + (self.image_shadows[tree[0]].width/8 if (tree[0] != 2) else self.image_shadows[tree[0]].width/50)
                self.image_shadows[tree[0]].y = y - (self.image_shadows[tree[0]].height/20 if (tree[0] == 2) else self.image_shadows[tree[0]].height)# - (self.image_shadows[tree[0]].height/1.4 if (tree[0] != 2) else self.image_shadows[tree[0]].height/4)
                drawp(self.image_shadows[tree[0]])
