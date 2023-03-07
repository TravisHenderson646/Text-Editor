'''
A simple text editor in pygame
'''

import pygame as pg

# Define some colors
BLACK = pg.Color(0, 0, 0)
WHITE = pg.Color(255, 255, 255)
GREY = pg.Color(200, 200, 200)
GREEN = pg.Color(69, 175, 100)
RED = pg.Color(175, 69, 125)
BLUE = pg.Color(69, 100, 175)

pg.init()
size = (1280,720)
screen = pg.display.set_mode(size)
pg.display.set_caption("My Game")
clock = pg.time.Clock()

class Block(pg.sprite.Sprite):
    def __init__(self, position, size, color=GREY): # position and size are lists of 2 [x,y]
        super().__init__()
        
        self.image = pg.Surface(size)
        self.image.fill(color)

        self.rect = self.image.get_rect(topleft=position)

        self.pos = pg.math.Vector2(0,0)

# Generate entities before loop

# Main Program Loop 
done = False
while not done:
    # User input
    for event in pg.event.get():
        if event.type == pg.QUIT:
            done = True

        elif event.type == pg.KEYDOWN:
            if event.key == pg.K_ESCAPE:
                done = True       
 
    # Game logic
 
    # Drawing code
    screen.fill(BLACK)

    pg.display.flip()
 
    clock.tick(60)
 
# Close the window and quit.
pg.quit()