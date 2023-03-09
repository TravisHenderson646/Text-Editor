import pygame as pg
from settings import *

def format_text(text, textbox_size, font):
    y = 0
    font_height = font.size("Tg")[1]
    textbox = pg.Surface((1280,720)) # magic number
    while text:
        #determine if the row fits vertically
        if y + font_height > textbox_size[1]:
            break

        #determine how many words fit
        i = 1
        j = 1
        while font.size(text[:i])[0] < textbox_size[0] and i < len(text) and text[i-1] != '☺':
            i += 1
            j += 1
        # if wrapped, slide i to just after prev space could add dashes
        if i < len(text):
            if max(text.rfind(' ', 0 , i) + 1,text.rfind('-', 0, i) + 1) > 0:
                i = max(text.rfind(' ', 0 , i) + 1,text.rfind('-', 0, i) + 1)
            else :
                i -= 1 #if single word is longer than entire line, break it up
        
        if text.rfind('☺', 0, j+1) > 0:
            i = text.rfind('☺', 0, j) + 1
            image = font.render(text[:i-1], True, COLOR)
            textbox.blit(image, (0, y))
        
        # render and blit line
        else:
            image = font.render(text[:i], True, COLOR)
            textbox.blit(image, (0, y))
            if i == len(text):
                pg.draw.line(textbox, GREY, (font.size(text[:i])[0], y), (font.size(text[:i])[0], y + font_height*.8), 3)
        
        y += font_height

        # remove text we just blitted for next iteration
        text = text[i:]


    return textbox # doesn't currently handle overflow text