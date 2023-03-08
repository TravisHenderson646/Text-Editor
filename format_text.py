import pygame as pg

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
        while font.size(text[:i])[0] < textbox_size[0] and i < len(text):
            i += 1
        
        # if wrapped, slide i to just after prev space
        try:
            if i < len(text):
                i = text.rindex(' ', 0 , i) + 1
        except:
            i -= 1
        

        # render and blit line
        image = font.render(text[:i], True, 'red')
        textbox.blit(image, (0, y))
        y += font_height

        # remove text we just blitted for next iteration
        text = text[i:]

    return textbox