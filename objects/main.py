pyglet.gl.glLineWidth(3)
pyglet.gl.glEnable (GL_LINE_SMOOTH)
pyglet.gl.glEnable(pyglet.gl.GL_BLEND)
pyglet.gl.glBlendFunc(pyglet.gl.GL_SRC_ALPHA, pyglet.gl.GL_ONE_MINUS_SRC_ALPHA)

pyglet.font.add_file('assets/font/pixel.ttf')

v = collision.Vector # для создания полигонов

engine_settings.on_text_bool           = False
engine_settings.on_mouse_motion_bool   = True
engine_settings.on_mouse_drag_bool     = True
engine_settings.on_key_press_bool      = True
engine_settings.on_mouse_press_bool    = True
engine_settings.on_mouse_release_bool  = True
engine_settings.on_draw_bool           = True
engine_settings.on_update_bool         = True

def off_input():
    engine_settings.on_text_bool           = False
    engine_settings.on_mouse_motion_bool   = True
    engine_settings.on_mouse_drag_bool     = False
    engine_settings.on_key_press_bool      = False
    engine_settings.on_mouse_press_bool    = False
    engine_settings.on_mouse_release_bool  = False
    engine_settings.on_draw_bool           = True
    engine_settings.on_update_bool         = True

def on_input():
    engine_settings.on_text_bool           = False
    engine_settings.on_mouse_motion_bool   = True
    engine_settings.on_mouse_drag_bool     = True
    engine_settings.on_key_press_bool      = True
    engine_settings.on_mouse_press_bool    = True
    engine_settings.on_mouse_release_bool  = True
    engine_settings.on_draw_bool           = True
    engine_settings.on_update_bool         = True

def show_cursor():
    window.set_mouse_visible(True)

def hide_cursor():
    window.set_mouse_visible(False)

def main():
    clear_display()
    add_display(text_label(settings.width//2, settings.height//2, 'HELLO WORLD', load_font=True, font='pixel.ttf', size=settings.height//20, anchor_x='center', color = (180, 180, 180, 255)))
