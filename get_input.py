import pygame as pg

def get_input(current_string, event, done):
    if event.type == pg.QUIT:
        done = True

    elif event.type == pg.KEYDOWN:
        if event.key == pg.K_ESCAPE:
            done = True
        
        if event.key == pg.K_q:
            current_string += 'q'
        if event.key == pg.K_w:
            current_string += 'w'
        if event.key == pg.K_e:
            current_string += 'e'
        if event.key == pg.K_r:
            current_string += 'r'

    return current_string, done