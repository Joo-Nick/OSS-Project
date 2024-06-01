# python game with pygame : Jumping dino
# by. BlockDMask
import pygame
import random
import sys
from src.dino import Dino
from src.obstacle import Tree, FlyingObstacle
from src.cloud import Cloud
from src.background import background

pygame.init()
pygame.display.set_caption('Jumping dino')
MAX_WIDTH = 800
MAX_HEIGHT = 400
screen = pygame.display.set_mode((MAX_WIDTH, MAX_HEIGHT))

def main():
    # 변수 설정
    fps = pygame.time.Clock()
    run = True
    gamespeed = 12

    # dino 인스턴스 생성
    dino = Dino()

    # tree 인스턴스 생성
    tree = Tree(screen, 'Python_dinosaur_game/images/Obstacle/Tree.png')

    # flying_obstacle 인스턴스 생성
    flying_obstacle = FlyingObstacle(screen, 'Python_dinosaur_game/images/Obstacle/FlyingObstacle.png')

    # Cloud 인스턴스 생성
    cloud = Cloud()

    while run:
        screen.fill((255, 255, 255))
        userinput = pygame.key.get_pressed()

        # event check
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        # tree move
        tree.move()

        # draw tree
        tree.draw()

        # flying obstacle move
        flying_obstacle.move()

        # draw flying obstacle
        flying_obstacle.draw()

        # draw dino
        dino.draw(screen)
        dino.dinoupdate(userinput)

        # draw cloud
        cloud.draw(screen)
        cloud.update()

        # background
        background()

        # update
        pygame.display.update()
        fps.tick(30)


def menu(death_count):
    global points
    run = True
    while run:
        font = pygame.font.Font('freesansbold.ttf', 30)
        RunDino = pygame.image.load('Python_dinosaur_game/images/Dino/DinoRun1.png')
        GameoverImg = pygame.image.load('Python_dinosaur_game/images/Other/Gameover.png')
        ResetImg = pygame.image.load('Python_dinosaur_game/images/Other/Reset.png')

        if death_count == 0:
            screen.fill((255, 255, 255))
            text = font.render("Press any Key to Start", True, (0, 0, 0))
            textRect = text.get_rect()
            textRect.center = (MAX_WIDTH // 2, MAX_HEIGHT // 2)
            screen.blit(text, textRect)
            screen.blit(RunDino, (MAX_WIDTH // 2 - 20, MAX_HEIGHT // 2 - 140))
        elif death_count > 0:
            gameoverRect = GameoverImg.get_rect()
            gameoverRect.center = (MAX_WIDTH // 2, MAX_HEIGHT // 2 - 50)
            resetRect = ResetImg.get_rect()
            resetRect.center = (MAX_WIDTH // 2, MAX_HEIGHT // 2 + 50)
            screen.blit(GameoverImg, gameoverRect)
            screen.blit(ResetImg,resetRect)

        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                main()


menu(death_count=0)
