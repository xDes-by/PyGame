from pygame import font, display, draw, mouse
from bin.precache import screen, carImg_3, BLACK, WIDTH_SCREEN, HEIGHT_SCREEN

import time


def things(thing_x, thing_y):
    screen.blit(carImg_3, (thing_x, thing_y))


def car(img, x, y):
    screen.blit(img, (x, y))


def text_objects(text, font_rend):
    textSurface = font_rend.render(text, True, BLACK)
    return textSurface, textSurface.get_rect()


def message_display(text):
    largeText = font.Font('freesansbold.ttf', 115)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((WIDTH_SCREEN / 2), (HEIGHT_SCREEN / 2))
    screen.blit(TextSurf, TextRect)

    display.update()

    time.sleep(2)
    from my_car_game import game_loop
    game_loop()


def things_dodged(count):
    font_text = font.SysFont(None, 25)
    text = font_text.render("Dodged: " + str(count), True, BLACK)
    screen.blit(text, (0, 0))


def crash():
    message_display("Разбился")


def button(msg, x, y, w, h, ic, ac, action=None):
    mouse_pos = mouse.get_pos()
    click = mouse.get_pressed()
    if x + w > mouse_pos[0] > x and y + h > mouse_pos[1] > y:
        draw.rect(screen, ac, (x, y, w, h))
        if click[0] == 1 and action is not None:
            action()
    else:
        draw.rect(screen, ic, (x, y, w, h))

    smallText = font.SysFont("comicsansms", 20)
    textSurf, textRect = text_objects(msg, smallText)
    textRect.center = ((x + (w / 2)), (y + (h / 2)))
    screen.blit(textSurf, textRect)
