import pygame as pg

def get_input(current_string, event, done):
    if event.type == pg.QUIT:
        done = True

    elif event.type == pg.KEYDOWN:
        if event.key == pg.K_ESCAPE:
            done = True
        
        if event.key == pg.K_BACKSPACE:
            current_string = current_string[:-1]
        if event.key == pg.K_SPACE:
            current_string += ' '
        if event.key == pg.K_RETURN:
            current_string += '☺'

        # if left or right shift is pressed w/+w/o caps lock
        if event.mod == 4097 or event.mod == 4098 or event.mod == 4099 or event.mod == 12289 or event.mod == 12290 or event.mod == 12291:
            if event.key == pg.K_1:
                current_string += '!'
            if event.key == pg.K_2:
                current_string += '@'
            if event.key == pg.K_3:
                current_string += '#'
            if event.key == pg.K_4:
                current_string += '$'
            if event.key == pg.K_5:
                current_string += '%'
            if event.key == pg.K_6:
                current_string += '^'
            if event.key == pg.K_7:
                current_string += '&'
            if event.key == pg.K_8:
                current_string += '*'
            if event.key == pg.K_9:
                current_string += '('
            if event.key == pg.K_0:
                current_string += ')'
            if event.key == pg.K_MINUS:
                current_string += '_'
            if event.key == pg.K_EQUALS:
                current_string += '+'
            if event.key == pg.K_BACKQUOTE:
                current_string += '~'
            if event.key == pg.K_LEFTBRACKET:
                current_string += '{'
            if event.key == pg.K_RIGHTBRACKET:
                current_string += '}'
            if event.key == pg.K_PERIOD:
                current_string += '>'
            if event.key == pg.K_COMMA:
                current_string += '<'
            if event.key == pg.K_QUOTE:
                current_string += '"'
            if event.key == pg.K_SEMICOLON:
                current_string += ':'
            if event.key == pg.K_BACKSLASH:
                current_string += '?'
            if event.key == pg.K_SLASH:
                current_string += '|'
        # if shift xor caps lock
        if event.mod == 4097 or event.mod == 4098 or event.mod == 4099 or event.mod == 12288:
            if event.key == pg.K_a:
                current_string += 'A'
            if event.key == pg.K_b:
                current_string += 'B'
            if event.key == pg.K_c:
                current_string += 'C'
            if event.key == pg.K_d:
                current_string += 'D'
            if event.key == pg.K_e:
                current_string += 'E'
            if event.key == pg.K_f:
                current_string += 'F'
            if event.key == pg.K_g:
                current_string += 'G'
            if event.key == pg.K_h:
                current_string += 'H'
            if event.key == pg.K_i:
                current_string += 'I'
            if event.key == pg.K_j:
                current_string += 'J'
            if event.key == pg.K_k:
                current_string += 'K'
            if event.key == pg.K_l:
                current_string += 'L'
            if event.key == pg.K_m:
                current_string += 'M'
            if event.key == pg.K_n:
                current_string += 'N'
            if event.key == pg.K_o:
                current_string += 'O'
            if event.key == pg.K_p:
                current_string += 'P'
            if event.key == pg.K_q:
                current_string += 'Q'
            if event.key == pg.K_r:
                current_string += 'R'
            if event.key == pg.K_s:
                current_string += 'S'
            if event.key == pg.K_t:
                current_string += 'T'
            if event.key == pg.K_u:
                current_string += 'U'
            if event.key == pg.K_v:
                current_string += 'V'
            if event.key == pg.K_w:
                current_string += 'W'
            if event.key == pg.K_x:
                current_string += 'X'
            if event.key == pg.K_y:
                current_string += 'Y'
            if event.key == pg.K_z:
                current_string += 'Z'
        # if no mods or shift and caps lock
        if event.mod == 4096 or event.mod == 12289 or event.mod == 12290 or event.mod == 12291:
            if event.key == pg.K_a:
                current_string += 'a'
            if event.key == pg.K_b:
                current_string += 'b'
            if event.key == pg.K_c:
                current_string += 'c'
            if event.key == pg.K_d:
                current_string += 'd'
            if event.key == pg.K_e:
                current_string += 'e'
            if event.key == pg.K_f:
                current_string += 'f'
            if event.key == pg.K_g:
                current_string += 'g'
            if event.key == pg.K_h:
                current_string += 'h'
            if event.key == pg.K_i:
                current_string += 'i'
            if event.key == pg.K_j:
                current_string += 'j'
            if event.key == pg.K_k:
                current_string += 'k'
            if event.key == pg.K_l:
                current_string += 'l'
            if event.key == pg.K_m:
                current_string += 'm'
            if event.key == pg.K_n:
                current_string += 'n'
            if event.key == pg.K_o:
                current_string += 'o'
            if event.key == pg.K_p:
                current_string += 'p'
            if event.key == pg.K_q:
                current_string += 'q'
            if event.key == pg.K_r:
                current_string += 'r'
            if event.key == pg.K_s:
                current_string += 's'
            if event.key == pg.K_t:
                current_string += 't'
            if event.key == pg.K_u:
                current_string += 'u'
            if event.key == pg.K_v:
                current_string += 'v'
            if event.key == pg.K_w:
                current_string += 'w'
            if event.key == pg.K_x:
                current_string += 'x'
            if event.key == pg.K_y:
                current_string += 'y'
            if event.key == pg.K_z:
                current_string += 'z'
        # if no mods or caps lock
        if event.mod == 4096 or event.mod == 12288:
            if event.key == pg.K_1:
                current_string += '1'
            if event.key == pg.K_2:
                current_string += '2'
            if event.key == pg.K_3:
                current_string += '3'
            if event.key == pg.K_4:
                current_string += '4'
            if event.key == pg.K_5:
                current_string += '5'
            if event.key == pg.K_6:
                current_string += '6'
            if event.key == pg.K_7:
                current_string += '7'
            if event.key == pg.K_8:
                current_string += '8'
            if event.key == pg.K_9:
                current_string += '9'
            if event.key == pg.K_0:
                current_string += '0'
            if event.key == pg.K_MINUS:
                current_string += '-'
            if event.key == pg.K_EQUALS:
                current_string += '='
            if event.key == pg.K_BACKQUOTE:
                current_string += '`'
            if event.key == pg.K_LEFTBRACKET:
                current_string += '['
            if event.key == pg.K_RIGHTBRACKET:
                current_string += ']'
            if event.key == pg.K_PERIOD:
                current_string += '.'
            if event.key == pg.K_COMMA:
                current_string += ','
            if event.key == pg.K_QUOTE:
                current_string += "'"
            if event.key == pg.K_SEMICOLON:
                current_string += ';'
            if event.key == pg.K_BACKSLASH:
                current_string += '\\'
            if event.key == pg.K_SLASH:
                current_string += '/'

    return current_string, done