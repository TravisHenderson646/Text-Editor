'''
A simple text editor in pygame
'''

import sys
import pygame as pg
from format_text import *
from get_input import *
import settings as sett

pg.init()

class Main:
    def __init__(self):
        self.screen = pg.display.set_mode(sett.SIZE)
        pg.display.set_caption("Edit Text")
        self.clock = pg.time.Clock()
        self.done = False

    # Main Program Loop
    def run(self):
        while not self.done:
            for event in pg.event.get():
                sett.MAIN_STRING, self.done = get_input(sett.MAIN_STRING, event, self.done)

            # logic
            formatted = format_text(sett.MAIN_STRING, sett.SIZE, sett.FONT)

            # Drawing code
            self.screen.fill(sett.BLACK)
            self.screen.blit(formatted, (0, 0))
            pg.display.flip()
        
            self.clock.tick(60)

        if sett.SAVE:
            with open('save.txt', 'w') as save_string:
                save_string.write(sett.MAIN_STRING)
        pg.quit()
        sys.exit()

if __name__ == '__main__':
    main = Main()
    main.run()
# Close the window and quit.


