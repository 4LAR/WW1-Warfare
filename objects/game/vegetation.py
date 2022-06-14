class vegetation():
    def __init__(self):

        self.tree_list = []
        self.images = [
            [image_label('world/vegetation/tree.png', 0 , 0, scale=settings.height/240), settings.height/2.7],
            [image_label('world/vegetation/tree_1.png', 0 , 0, scale=settings.height/240), 0],#settings.height/2.7
            [image_label('world/vegetation/tree_2.png', 0 , 0, scale=settings.height/240), settings.height/3.9],
            [image_label('world/vegetation/tree_3.png', 0 , 0, scale=settings.height/240), settings.height/2.7]
        ]

        self.tree_list.append([0, 10])
        self.tree_list.append([3, 30])
        self.tree_list.append([0, 50])
        self.tree_list.append([1, 100])
        self.tree_list.append([2, 150])

    def update(self):
        pass

    def draw(self):
        for tree in self.tree_list:
            self.images[tree[0]][0].sprite.x = get_obj_display('world').pos_with_world(tree[1]) + get_obj_display('world').move_x + get_obj_display('world').map_offs[0]
            self.images[tree[0]][0].sprite.y = get_obj_display('world').map_offs[1] - get_obj_display('world').fov/2 + self.images[tree[0]][1]
            drawp(self.images[tree[0]][0])
