
SCALE_WORLD = settings.height/240

SHADOWS_DEG = -120
SHADOWS_COLOR = (0, 0, 0, 80)

def image_transform_for_shadow(image_name, shadows_color):
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

def add_game_classes(menu=False):
    add_display(world(menu=menu))
    #add_display(clouds())
    add_display(trenches())
    add_display(dot())
    add_display(parties_flag())
    add_display(vegetation())
    add_display(fog())
    add_display(gui())

def play():
    clear_display()
    add_game_classes()

    #add_display(text_label(settings.width//2, settings.height//2, 'HELLO WORLD', load_font=True, font='pixel.ttf', size=settings.height//20, anchor_x='center', color = (180, 180, 180, 255)))
