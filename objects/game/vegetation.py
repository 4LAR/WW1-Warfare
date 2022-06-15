class vegetation():
    def __init__(self):

        self.tree_list = []
        self.images = [
            [image_label('world/vegetation/tree.png', 0 , 0, scale=settings.height/240), settings.height/2.7, 0],
            [image_label('world/vegetation/tree_1.png', 0 , 0, scale=settings.height/240), settings.height/2.7, 0],
            [image_label('world/vegetation/tree_2.png', 0 , 0, scale=settings.height/240), settings.height/3.9, -settings.height/8],
            [image_label('world/vegetation/tree_3.png', 0 , 0, scale=settings.height/240), settings.height/2.7, 0]
        ]

        self.tree_list.append([0, 10, 0])
        self.tree_list.append([3, 30, 0])
        self.tree_list.append([0, 50, 0])
        self.tree_list.append([1, 100, 0])
        self.tree_list.append([2, 150, 0])

        self.tree_list.append([0, 5, 1])
        self.tree_list.append([0, 30, 1])
        self.tree_list.append([3, 60, 1])

        self.tree_list.append([1, 150, 1])
        self.tree_list.append([2, 200, 1])

    def update(self):
        pass

    def draw(self):
        for tree in self.tree_list:
            self.images[tree[0]][0].sprite.x = get_obj_display('world').pos_with_world(tree[1]) + get_obj_display('world').move_x + get_obj_display('world').map_offs[0] * (1.2 if (tree[2] == 1) else 1)
            self.images[tree[0]][0].sprite.y = get_obj_display('world').map_offs[1] - get_obj_display('world').fov/2 + self.images[tree[0]][tree[2] + 1]
            drawp(self.images[tree[0]][0])
