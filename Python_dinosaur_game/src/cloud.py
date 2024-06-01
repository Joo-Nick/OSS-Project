import pygame
import random

MAX_WIDTH = 800
gamespeed = 12

class Cloud:
    def __init__(self):
        CLOUD = pygame.image.load('Python_dinosaur_game/images/Other/Cloud.png')
        self.x = MAX_WIDTH + random.randint(500, 700)
        self.y = random.randint(50, 100)
        self.image = CLOUD
        self.width = self.image.get_width()

    def update(self):
        self.x -= gamespeed
        if self.x < -self.width:
            self.x = MAX_WIDTH + random.randint(1300, 1700)
            self.y = random.randint(50, 100)

    def draw(self, SCREEN):
        SCREEN.blit(self.image, (self.x, self.y))