import pygame
import random

class Obstacle_random:
    def __init__(self, screen, img_path, speed, start_y, y_pos_bg): # y_pos_bg는 src/background.py의 높이
        self.screen = screen
        self.image = pygame.image.load(img_path)
        self.rect = self.image.get_rect()  # 이미지의 사각형 충돌 영역
        self.x = screen.get_width()  # 화면의 너비를 가져와 시작 위치 사용
        self.y = start_y
        self.speed = speed
        self.y_pos_bg = y_pos_bg

    def move_random(self):
        self.x -= self.speed
        self.rect.topleft = (self.x, self.y)  # 이미지 위치에 맞게 충돌 영역 업데이트
    
    def draw_random(self):
        self.screen.blit(self.image, self.rect.topleft)
        
class Trap(Obstacle_random):
    def __init__(self, screen, img_path='Python_dinosaur_game/images/Obstacle/Trap.png', y_pos_bg=330):
        super().__init__(screen, img_path, 12, y_pos_bg+5, y_pos_bg)  # 속도 조정하여 tree와 같은 속도로 움직이도록 함
        self.initial_x = self.x  # 트랩 생성 시 x 좌표 저장
        self.tree_x = 0
        
    def move_random(self):
        super().move_random()
        if self.x <= self.initial_x - self.screen.get_width():  # 초기 위치에서 화면 너비만큼 이동했을 때 삭제
            return False  # 삭제 신호 반환
        return True  # 유지 신호 반환
    
    def set_tree_x(self, tree_x):
        self.tree_x = tree_x
    
    def generate_random_x(self):
        min_x = self.tree_x + 195  # 나무의 x 좌표에서 +- 250만큼
        max_x = self.tree_x + 605 
        return random.randint(min_x, max_x)  # 위 범위에서 랜덤한 x 좌표 생성
        