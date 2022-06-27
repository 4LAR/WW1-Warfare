#
#
#
#

# bg color
# HEX: #3A3945
# RGB: (58, 57, 69)

# text color
# HEX: #B6B3A6
# RGB: (182, 179, 166)
# font: urod.ttf

import time

window.set_icon(pyglet.image.load('assets/img/stone_engine.png'))

class skip():
	def __init__(self, type=0):
		self.type = type

	def on_key_press(self, symbol, modifiers):
		if symbol == pyglet.window.key.ESCAPE:
			if self.type == 0:
				main()
			return pyglet.event.EVENT_HANDLED
		elif symbol == pyglet.window.key.SPACE:
			if self.type == 0:
				main()
		return True

def add_timer_text_logo():
	add_display(breathing_label(0, 0, settings.width, settings.height, (0, 0, 0), 0, delay=0.04, function=main, for_from=0, for_before=255, tick=5))

if settings.game_options['draw_logo']:
	hide_cursor()
	add_display(skip())
	add_display(label(0, 0, settings.width, settings.height, (58, 57, 69)))
	add_display(image_label('logo_studio.png', settings.width/2, settings.height/2, scale=settings.height/100, pixel=True, center=True))
	add_display(breathing_label(0, 0, settings.width, settings.height, (58, 57, 69), 0, delay=0.04, function=add_timer_text_logo))

else:
	main()

def text_logo():
	clear_display()
	add_display(skip())
	add_display(label(settings.width, settings.height, settings.width, settings.height, (0, 0, 0)))
	add_display(text_label(settings.width//2, settings.height//2, 'This project is under development.', load_font=True, font='pixel.ttf', size=settings.height//20, anchor_x='center', color = (180, 180, 180, 255)))
	add_display(text_label(settings.width//2, settings.height//2 - settings.height//19, 'It will improve with each update.', load_font=True, font='pixel.ttf', size=settings.height//20, anchor_x='center', color = (180, 180, 180, 255)))
	add_display(breathing_label(0, 0, settings.width, settings.height, (0, 0, 0), 0, delay=0.04, function=add_timer_text_logo))
