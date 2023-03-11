import pygame as pg
pg.font.init()


with open('save.txt', 'r') as save_string:
    MAIN_STRING = save_string.read()

SAVE = True

SIZE = (1280//2 + 160, 720)
TEXTBOX_SIZE = (1280//2, 720)
FONT_SIZE = 80
FONTS_LIST = pg.font.get_fonts()
CURRENT_FONT = -1
FONT = pg.font.SysFont(None,FONT_SIZE)

# Define some colors

BLACK = pg.Color(0, 0, 0)
WHITE = pg.Color(255, 255, 255)
GREY = pg.Color(200, 200, 200)
GREEN = pg.Color(69, 175, 100)
RED = pg.Color(175, 69, 125)
BLUE = pg.Color(69, 100, 175)
COLOR = -1
COLOR_LIST = [BLACK, WHITE, GREY, GREEN, RED, BLUE]