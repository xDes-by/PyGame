import sys
import random
import pygame
import time as game_time

from bin.precache import *
from bin.functions import text_objects, button, crash, things, things_dodged, car

pygame.init()


def game_intro():
    intro = True
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        screen.fill(WHITE)
        largeText = pygame.font.Font('freesansbold.ttf', 50)
        TextSurf, TextRect = text_objects("Don't crash my car", largeText)
        TextRect.center = ((WIDTH_SCREEN / 2), (HEIGHT_SCREEN / 2))
        screen.blit(TextSurf, TextRect)

        button("GO!", 150, 450, 100, 50, GREEN, GREEN_2, game_loop)

        pygame.display.update()
        clock.tick(15)


def game_loop():
    start_time = game_time.time()
    x = WIDTH_SCREEN * 0.6
    y = HEIGHT_SCREEN * 0.8

    x_2 = WIDTH_SCREEN * 0.4
    y_2 = HEIGHT_SCREEN * 0.8

    x_change = 0
    x_2_change = 0

    game_exit = False

    thing_start_x = random.randrange(0, WIDTH_SCREEN)
    thing_start_y = -600
    thing_speed = 5
    thing_width = 45
    thing_height = 80
    dodge_thing = 0

    while not game_exit:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                if event.key == pygame.K_LEFT:
                    x_change -= 5
                if event.key == pygame.K_RIGHT:
                    x_change += 5
                if event.key == pygame.K_a:
                    x_2_change -= 5
                if event.key == pygame.K_d:
                    x_2_change += 5
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0
                if event.key == pygame.K_a or event.key == pygame.K_d:
                    x_2_change = 0

        if x > WIDTH_SCREEN - car_width or x < 0:
            crash(start_time, dodge_thing)
            game_exit = True
        if x_2 > WIDTH_SCREEN - car_width or x_2 < 0:
            crash(start_time, dodge_thing)
            game_exit = True

        if y < thing_start_y + thing_height:
            if thing_start_x < x < thing_start_x + thing_width or thing_start_x < x + car_width < thing_start_x + thing_width:
                crash(start_time, dodge_thing)

        if y_2 < thing_start_y + thing_height:
            if thing_start_x < x_2 < thing_start_x + thing_width or thing_start_x < x_2 + car_width < thing_start_x + thing_width:
                crash(start_time, dodge_thing)

        if thing_start_y > HEIGHT_SCREEN:
            thing_start_y = 0 - thing_height
            thing_start_x = random.randrange(0, WIDTH_SCREEN)
            dodge_thing += 1
            thing_speed += 1

        x += x_change
        x_2 += x_2_change

        screen.fill(WHITE)

        things(thing_start_x, thing_start_y)
        thing_start_y += thing_speed

        things_dodged(dodge_thing)
        car(carImg, x, y)
        car(carImg_2, x_2, y_2)
        pygame.display.update()


game_intro()
pygame.quit()
sys.exit()
