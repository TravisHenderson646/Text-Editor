import pygame as pg
pg.font.init()

SAVE = True

SIZE = (1280//2,720)
FONT_SIZE = 80
FONTS_LIST = [i for i in pg.font.get_fonts()]
FONT = pg.font.SysFont(None,FONT_SIZE)

# Define some colors
BLACK = pg.Color(0, 0, 0)
WHITE = pg.Color(255, 255, 255)
GREY = pg.Color(200, 200, 200)
GREEN = pg.Color(69, 175, 100)
RED = pg.Color(175, 69, 125)
BLUE = pg.Color(69, 100, 175)
COLOR = BLUE