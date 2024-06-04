import pygame

# 게임의 레벨을 관리, 점수별로 레벨 갱신

class LevelManager:
    def __init__(self):
        self.level = 0

    def update_level(self, score):
        if score >= 2000:
            self.level = 5
        elif score >= 1500:
            self.level = 4
        elif score >= 1000:
            self.level = 3
        elif score >= 500:
            self.level = 2
        elif score >= 100:
            self.level = 1
        else:
            self.level = 0

    def get_level(self):
        return self.level
