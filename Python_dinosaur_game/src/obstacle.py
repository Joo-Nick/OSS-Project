import pygame

class Tree:
    def __init__(self, screen, img_path='Python_dinosaur_game/images/tree.png', max_width=800, max_height=600):
        self.screen = screen
        self.image = pygame.image.load(img_path)
        
        tree_height = self.image.get_size()[1]
        
        self.x = max_width
        self.y = max_height - tree_height
        self.speed = 12.0 # 나중에 플레이 시간에 따른 점수 연계해서 속도 변경

    def move(self):
        self.x -= self.speed
        if self.x <= 0:
            self.x = 800

    def draw(self):
        self.screen.blit(self.image, (self.x, self.y))