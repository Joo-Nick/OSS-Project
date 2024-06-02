import pygame
import random

class Obstacle:
    def __init__(self, screen, img_path, speed, start_y, y_pos_bg): # y_pos_bg는 src/background.py의 높이
        self.screen = screen
        self.image = pygame.image.load(img_path)
        self.rect = self.image.get_rect()  # 이미지의 사각형 충돌 영역
        self.x = screen.get_width()  # 화면의 너비를 가져와 시작 위치 사용
        self.y = start_y
        self.speed = speed
        self.y_pos_bg = y_pos_bg

    def move(self):
        self.x -= self.speed
        if self.x <= 0:
            self.x = self.screen.get_width()
        self.rect.topleft = (self.x, self.y)  # 이미지 위치에 맞게 충돌 영역 업데이트
    
    def draw(self):
        self.screen.blit(self.image, self.rect.topleft)

class Tree(Obstacle):
    def __init__(self, screen, img_path='Python_dinosaur_game/images/Obstacle/Tree.png', y_pos_bg=330): 
        tree_height = pygame.image.load(img_path).get_height()
        super().__init__(screen, img_path, 12, y_pos_bg - tree_height + 10, y_pos_bg) # + 10은 images/Other/Track.png 이미지의 위쪽 공백에 대한 보정

class FlyingObstacle(Obstacle):
    def __init__(self, screen, img_path='Python_dinosaur_game/images/Obstacle/FlyingObstacle.png', y_pos_bg=330):
        super().__init__(screen, img_path, 7, 0, y_pos_bg)  
        self.direction = 1  # 지그재그 움직임을 위한 방향 변수

    def move(self):
        super().move()
        self.y += self.direction * 12  # 세로방향의 속도
        if self.y <= 0 or self.y >= (self.y_pos_bg - self.image.get_height()):  # 상하 이동 범위 제한
            self.direction *= -1  # 방향 전환
            
class Trap(Obstacle):
    def __init__(self, screen, img_path='Python_dinosaur_game/images/Obstacle/Trap.png', y_pos_bg=330):
        super().__init__(screen, img_path, 12, y_pos_bg - 20, y_pos_bg)  # 속도 조정하여 tree와 같은 속도로 움직이도록 함
        self.x = screen.get_width() - 300  # 트랩이 트리 옆에 위치하도록 x 위치 조정