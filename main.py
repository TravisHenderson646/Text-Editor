'''
A simple text editor in pygame
'''

import sys
import pygame as pg
from format_text import *
from get_input import *
from settings import *

pg.init()

class Main:
    def __init__(self):
        self.screen = pg.display.set_mode(SIZE)
        pg.display.set_caption("Edit Text")
        self.clock = pg.time.Clock()
        with open('save.txt', 'r') as save_string:
            self.main_string = save_string.read()
        self.done = False

    # Main Program Loop
    def run(self):
        while not self.done:
            for event in pg.event.get():
                self.main_string, self.done = get_input(self.main_string, event, self.done)

            # logic
            formatted = format_text(self.main_string, SIZE, FONT)

            # Drawing code
            self.screen.fill(BLACK)
            self.screen.blit(formatted, (0, 0))
            pg.display.flip()
        
            self.clock.tick(60)

        if SAVE:
            with open('save.txt', 'w') as save_string:
                save_string.write(self.main_string)
        pg.quit()
        sys.exit()

if __name__ == '__main__':
    main = Main()
    main.run()
# Close the window and quit.


