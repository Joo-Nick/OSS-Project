import pygame
import os

# 게임의 목숨을 관리

class LifeManager:
    def __init__(self, initial_lives=3):
        self.lives = initial_lives
        self.invincible = False
        self.invincible_start_time = 0

    def lose_life(self):
        if self.lives > 0:
            self.lives -= 1
            self.invincible = True
            self.invincible_start_time = pygame.time.get_ticks()

    def is_alive(self):
        return self.lives > 0

    def reset_lives(self):
        self.lives = 3

    def get_lives(self):
        return self.lives

    def update_invincibility(self):
        current_time = pygame.time.get_ticks()
        if self.invincible and current_time - self.invincible_start_time > 1000:
            self.invincible = False

    def is_invincible(self):
        return self.invincible