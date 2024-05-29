import pygame

class Tree:
    def __init__(self, screen, img_path='Python_dinosaur_game/images/tree.png', max_width=800, max_height=600):
        self.screen = screen
        self.image = pygame.image.load(img_path)
        
        tree_height = self.image.get_height()
        
        self.x = max_width
        self.y = max_height - tree_height
        self.speed = 12

    def move(self):
        self.x -= self.speed
        if self.x <= 0:
            self.x = 800

    def draw(self):
        self.screen.blit(self.image, (self.x, self.y))
        
class FlyingObstacle:
    def __init__(self, screen, img_path='Python_dinosaur_game/images/flying_obstacle.png', max_width=800, max_height=400):
        self.screen = screen
        self.image = pygame.image.load(img_path)
        self.x = max_width
        self.y = 0  # 화면의 상단에서 시작
        self.speed = 7
        self.direction = 1  # 지그재그 움직임을 위한 방향 변수

    def move(self):
        self.x -= self.speed # 가로방향의 속도
        self.y += self.direction * 12  # 세로방향의 속도
        if self.y <= 0 or self.y >= (300 - self.image.get_height()):  # 상하 이동 범위 제한
            self.direction *= -1  # 방향 전환

        if self.x <= 0:
            self.x = 800

    def draw(self):
        self.screen.blit(self.image, (self.x, self.y))