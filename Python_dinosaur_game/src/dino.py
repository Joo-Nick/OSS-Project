import pygame
import os

class Dino:
    dino_x = 10
    dino_y = 265
    dino_y_duck = 295
    JUMP_VEL = 7.5

    def __init__(self):
        base_path = os.path.dirname(__file__)
        self.base_path = base_path
        self.RunDinoImg = [pygame.image.load(os.path.join(base_path, '../images/Dino/DinoRun1.png')),
                           pygame.image.load(os.path.join(base_path, '../images/Dino/DinoRun2.png'))]
        self.JumpDinoImg = pygame.image.load(os.path.join(base_path, '../images/Dino/DinoJump.png'))
        self.DuckDinoImg = [pygame.image.load(os.path.join(base_path, '../images/Dino/DinoDuck1.png')),
                            pygame.image.load(os.path.join(base_path, '../images/Dino/DinoDuck2.png'))]
        self.DeadDinoImg = pygame.image.load(os.path.join(base_path, '../images/Dino/DinoDead.png'))

        self.dino_duck = False
        self.dino_run = True
        self.dino_jump = False
        self.dino_dead = False

        self.step_index = 0
        self.jump_vel = self.JUMP_VEL
        self.image = self.RunDinoImg[0]

        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = self.dino_x
        self.dino_rect.y = self.dino_y
        self.dino_rect.width = 50  # 공룡 rect 너비 조정
        self.dino_rect.height = 80  # 공룡 rect 높이 조정

    def dinoupdate(self, userInput):
        if self.dino_duck:
            self.duck()
        if self.dino_run:
            self.run()
        if self.dino_jump:
            self.jump()
        if self.dino_dead:
            self.dead()

        if self.step_index >= 10:
            self.step_index = 0

        if userInput[pygame.K_UP] or userInput[pygame.K_SPACE] and not self.dino_jump: # 점프 키 지정
            self.dino_duck = False
            self.dino_run = False
            self.dino_jump = True
            self.dino_rect.y = self.dino_y # 점프키 공중부양 방지
        elif userInput[pygame.K_DOWN] and not self.dino_jump: # 슬라이딩 키 지정
            self.dino_duck = True
            self.dino_run = False
            self.dino_jump = False
        elif self.dino_jump and userInput[pygame.K_DOWN]:
            self.dino_rect.y += self.jump_vel * 4  # 내려오는 속도 크게 증가
            self.jump_vel -= 1.0
            self.dino_run = False
            self.dino_duck = True
        elif not (self.dino_jump or userInput[pygame.K_DOWN]):
            self.dino_duck = False
            self.dino_run = True
            self.dino_jump = False

    def duck(self): # 슬라이딩
        self.image = self.DuckDinoImg[self.step_index // 5]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = self.dino_x
        self.dino_rect.y = self.dino_y_duck
        self.step_index += 1
        self.dino_rect.width = 80  # 공룡 rect 너비 조정
        self.dino_rect.height = 50  # 공룡 rect 높이 조정


    def run(self): # 달리기
        self.image = self.RunDinoImg[self.step_index // 5]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = self.dino_x
        self.dino_rect.y = self.dino_y
        self.step_index += 1
        self.dino_rect.width = 50  # 공룡 rect 너비 조정
        self.dino_rect.height = 80  # 공룡 rect 높이 조정


    def jump(self): # 점프
        self.image = self.JumpDinoImg
        if self.dino_jump:
            self.dino_rect.y -= self.jump_vel * 4
            self.jump_vel -= 0.8
        if self.jump_vel < - self.JUMP_VEL:
            self.dino_jump = False
            self.jump_vel = self.JUMP_VEL
        self.dino_rect.width = 50  # 공룡 rect 너비 조정
        self.dino_rect.height = 80  # 공룡 rect 높이 조정

    def dead(self):
        self.image = self.DeadDinoImg
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = self.dino_x
        self.dino_rect.y = self.dino_y
        
    def draw(self, SCREEN):
        SCREEN.blit(self.image, (self.dino_rect.x, self.dino_rect.y))
        pygame.draw.rect(SCREEN, (255, 0, 0), self.dino_rect, 2)  # 공룡 rect 그리기
