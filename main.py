'''
A simple text editor in pygame
'''

import sys
import pygame as pg
from format_text import *
from get_input import *

SIZE = (1280,720)

# Define some colors
BLACK = pg.Color(0, 0, 0)
WHITE = pg.Color(255, 255, 255)
GREY = pg.Color(200, 200, 200)
GREEN = pg.Color(69, 175, 100)
RED = pg.Color(175, 69, 125)
BLUE = pg.Color(69, 100, 175)

class Block(pg.sprite.Sprite):
    def __init__(self, position, size, color=GREY): # position and size are lists of 2 [x,y]
        super().__init__()
        
        self.image = pg.Surface(size)
        self.image.fill(color)

        self.rect = self.image.get_rect(topleft=position)

        self.pos = pg.math.Vector2(0,0)

class Main:
    def __init__(self):
        pg.init()
        self.screen = pg.display.set_mode(SIZE)
        pg.display.set_caption("Edit Text")
        self.clock = pg.time.Clock()
        self.main_string = ''
        self.done = False

    # Main Program Loop 
    def run(self):
        while not self.done:
            # User input
            for event in pg.event.get():
                self.main_string, self.done = get_input(self.main_string, event, self.done)

        
            # logic

        
            # Drawing code
            self.screen.fill(BLACK)
            print(self.main_string)

            pg.display.flip()
        
            self.clock.tick(1)
        pg.quit()
        sys.exit()


if __name__ == '__main__':
    main = Main()
    main.run()
# Close the window and quit.


