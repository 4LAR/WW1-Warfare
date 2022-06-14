
def play():
    clear_display()
    add_display(world())
    #add_display(clouds())
    add_display(vegetation())
    add_display(trenches())
    add_display(gui())

    #add_display(text_label(settings.width//2, settings.height//2, 'HELLO WORLD', load_font=True, font='pixel.ttf', size=settings.height//20, anchor_x='center', color = (180, 180, 180, 255)))
