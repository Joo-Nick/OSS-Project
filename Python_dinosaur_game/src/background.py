import pygame
import random

MAX_WIDTH = 800
MAX_HEIGHT = 400
gamespeed = 12
screen = pygame.display.set_mode((MAX_WIDTH, MAX_HEIGHT))
x_pos_bg = 0
y_pos_bg = 330

BG = pygame.image.load('Python_dinosaur_game/images/Other/Track.png')

def background():
    global x_pos_bg, y_pos_bg
    image_width = BG.get_width()
    screen.blit(BG, (x_pos_bg, y_pos_bg))
    screen.blit(BG, (image_width + x_pos_bg, y_pos_bg))
    if x_pos_bg <= -image_width:
        screen.blit(BG, (image_width + x_pos_bg, y_pos_bg))
        x_pos_bg = 0
    x_pos_bg -= gamespeed
