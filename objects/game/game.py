

def image_transform_for_shadow(image_name, shadows_color, pil_image = False):
    if pil_image:
        img = get_pil_color_mask(image_name.transpose(Image.FLIP_TOP_BOTTOM), shadows_color)
    else:
        img = get_pil_color_mask(Image.open(image_name).transpose(Image.FLIP_TOP_BOTTOM), shadows_color)

    width, height = img.size
    img = img.resize((width, int(height/1.5)), Image.NEAREST)

    width, height = img.size
    m = -0.5
    xshift = abs(m) * width
    new_width = width + int(round(xshift))
    img = img.transform((new_width, height), Image.AFFINE,
            (1, m, -xshift if m > 0 else 0, 0, 1, 0), Image.NEAREST)

    return img

def add_game_classes(menu=False, map_name='test_summer'):
    add_display(world_save(map_name))
    add_display(game_rule())
    add_display(world(menu=menu))
    add_display(vegetation())
    add_display(clouds())
    add_display(trenches())
    add_display(vegetation_up_shadows())
    add_display(units())
    add_display(vegetation_middle())
    add_display(dot())
    add_display(parties_flag())
    add_display(units_down())
    add_display(vegetation_down())
    add_display(fog())
    add_display(rope())
    add_display(gui())
    add_display(pause_gui())
    add_display(game_info())
    if not menu:
        add_display(bot_player())

shoot_sound = Sound()
shoot_sound.update()

def play(map_name='test_summer'):
    on_input()
    clear_display()
    add_game_classes(map_name=map_name)
    add_display(breathing_label(0, 0, settings.width, settings.height, (0, 0, 0), 0, delay=0.01, for_from=255, for_before=0, tick=-5))

def play_breath(map_name='test_summer'):
    off_input()
    add_display(breathing_label(0, 0, settings.width, settings.height, (0, 0, 0), 0, delay=0.01, for_from=0, for_before=255, tick=5, arg='play(\'%s\')' % map_name))
