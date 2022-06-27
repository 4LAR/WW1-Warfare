#
#
#
#

import screeninfo
import configparser
import os
import pyglet

from console import *

def get_bool(str):
    return True if str.lower() == 'true' else False

class settings(console_term):
    def __init__(self):
        super().__init__()

        self.path = 'settings.ini'
        self.update_options = True

        self.error_promt = 'SETTINGS: '

        self.engine_options = {
            'width': screeninfo.get_monitors()[0].width,
            'height': screeninfo.get_monitors()[0].height,
            'full_screen': 1, # 0 - окно с рамками, 1 - окно без рамок, полный экран (не стабильно)
            'fps': 120,
            'show_fps': False,
            'console': False,
            'sound_volume': 0.4
        }

        self.pyglet_options = {
            'advanced_font_features': False,
            #'audio': ('xaudio2', 'directsound', 'openal', 'pulse', 'silent'),
            'darwin_cocoa': True,
            'debug_font': False,
            'debug_gl': True,
            'debug_gl_trace': False,
            'debug_gl_trace_args': False,
            'debug_graphics_batch': False,
            'debug_lib': False,
            'debug_media': False,
            'debug_texture': False,
            'debug_trace': False,
            'debug_trace_args': False,
            'debug_trace_depth': 1,
            'debug_trace_flush': True,
            'debug_win32': False,
            'debug_x11': False,
            'graphics_vbo': True,
            'headless': False,
            'headless_device': 0,
            'search_local_libs': True,
            'shadow_window': True,
            'vsync': True, # None,
            'win32_disable_shaping': False,
            'xlib_fullscreen_override_redirect': False,
            'xsync': True
        }

        self.game_options = {}

        self.read_settings()
        self.activate_engine_settings()

    def add_game_options(self, dict):
        self.game_options = dict
        self.read_settings(True)

    def activate_engine_settings(self):
        for conf in self.engine_options:
            exec('settings.%s = %s' % (conf, self.engine_options[conf]))

    def save_settings(self):
        config = configparser.ConfigParser()

        config.add_section("Engine")
        for conf in self.engine_options:
            config.set("Engine", str(conf), str(self.engine_options[conf]))

        config.add_section("Pyglet")
        for conf in self.pyglet_options:
            config.set("Pyglet", str(conf), str(self.pyglet_options[conf]))

        config.add_section("Game")
        for conf in self.game_options:
            config.set("Game", str(conf), str(self.game_options[conf]))

        with open(self.path, "w") as config_file:
            config.write(config_file)

        self.print(str(self.error_promt) + 'The settings have been saved to a file <<%s>>' % (self.path), 1)

    def read_settings(self, game_options_bool=False):
        if not os.path.exists(self.path): # проверка файла с настройками
            self.save_settings()
            self.read_settings()

        else:
            config = configparser.ConfigParser()
            config.read(self.path)

            #if ( screeninfo.get_monitors()[0].width >= int(config.get("Engine", "width")) and screeninfo.get_monitors()[0].height >= int(config.get("Engine", "height"))):
            #    self.width = int(config.get("Engine", "width"))
            #    self.height = int(config.get("Engine", "height"))

            #else:
            #    self.print(str(self.error_promt) + 'The screen resolution is incorrectly specified', 2)

            error_bool = False

            if not game_options_bool:
                for conf in self.engine_options:
                    try:
                        conf_buf = config.get("Engine", str(conf))
                        self.engine_options[conf] = conf_buf
                    except:
                        self.print(str(self.error_promt) + 'Error read argument (%s: %s)' % ('Engine', conf), 3)
                        error_bool = True

                for conf in self.pyglet_options:
                    try:
                        conf_buf = config.get("Pyglet", str(conf))
                        self.pyglet_options[conf] = get_bool(conf_buf) if (type(self.pyglet_options[conf]) == bool) else float(conf_buf)
                    except:
                        self.print(str(self.error_promt) + 'Error read argument (%s: %s)' % ('Pyglet', conf), 3)
                        error_bool = True

            else:
                for conf in self.game_options:
                    try:
                        conf_buf = config.get("Game", str(conf))
                        self.game_options[conf] = get_bool(conf_buf) if (type(self.game_options[conf]) == bool) else float(conf_buf)
                    except:
                        self.print(str(self.error_promt) + 'Error read argument (%s: %s)' % ('Game', conf), 3)
                        error_bool = True

            if error_bool and self.update_options:
                self.save_settings()
