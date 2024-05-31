import pygame

class Dino:
    dino_x = 10
    dino_y = 265
    dino_y_duck = 295
    JUMP_VEL = 6.5

    def __init__(self):
        self.RunDinoImg = [pygame.image.load('Python_dinosaur_game/images/Dino/DinoRun1.png'),
                        pygame.image.load('Python_dinosaur_game/images/Dino/DinoRun2.png')]
        self.JumpDinoImg = pygame.image.load('Python_dinosaur_game/images/Dino/DinoJump.png')
        self.DuckDinoImg = [pygame.image.load('Python_dinosaur_game/images/Dino/DinoDuck1.png'),
                        pygame.image.load('Python_dinosaur_game/images/Dino/DinoDuck2.png')]

        self.dino_duck = False
        self.dino_run = True
        self.dino_jump = False

        self.step_index = 0
        self.jump_vel = self.JUMP_VEL
        self.image = self.RunDinoImg[0]

        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = self.dino_x
        self.dino_rect.y = self.dino_y

    def dinoupdate(self, userInput): # 키 지정
        if self.dino_duck:
            self.duck()
        if self.dino_run:
            self.run()
        if self.dino_jump:
            self.jump()

        if self.step_index >= 10:
            self.step_index = 0

        if userInput[pygame.K_UP] and not self.dino_jump:
            self.dino_duck = False
            self.dino_run = False
            self.dino_jump = True
        elif userInput[pygame.K_DOWN] and not self.dino_jump:
            self.dino_duck = True
            self.dino_run = False
            self.dino_jump = False
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

    def run(self): # 달리기
        self.image = self.RunDinoImg[self.step_index // 5]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = self.dino_x
        self.dino_rect.y = self.dino_y
        self.step_index += 1

    def jump(self): # 점프
        self.image = self.JumpDinoImg
        if self.dino_jump:
            self.dino_rect.y -= self.jump_vel * 4
            self.jump_vel -= 0.8
        if self.jump_vel < - self.JUMP_VEL:
            self.dino_jump = False
            self.jump_vel = self.JUMP_VEL

    def draw(self, SCREEN):
        SCREEN.blit(self.image, (self.dino_rect.x, self.dino_rect.y))