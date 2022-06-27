pyglet.gl.glLineWidth(3)
pyglet.gl.glEnable (GL_LINE_SMOOTH)
pyglet.gl.glEnable(pyglet.gl.GL_BLEND)
pyglet.gl.glBlendFunc(pyglet.gl.GL_SRC_ALPHA, pyglet.gl.GL_ONE_MINUS_SRC_ALPHA)

pyglet.font.add_file('assets/font/urod.ttf')

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

settings_dict = {
    'shadows_transparency': 80,
    'shadows_angle': -120,
    'game_cursor': True,
    'game_parallax': True,
    'game_shadows': True,
    'draw_rope': False,
    'draw_logo': True
}

settings.add_game_options(settings_dict)

SCALE_WORLD = settings.height/240

BUTTONS_FONT_SCALE = 10;
BUTTONS_FONT_COLOR = (182, 179, 166, 255)

SHADOWS_DEG = settings.game_options['shadows_angle']
SHADOWS_COLOR = (0, 0, 0, int(settings.game_options['shadows_transparency']))

def main():
    window.set_icon(pyglet.image.load('assets/img/logo_game.png'))
    menu()
    #play()
