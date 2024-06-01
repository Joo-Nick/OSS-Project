# python game with pygame : Jumping dino
# by. BlockDMask
import pygame
import random
import sys
from src.obstacle import Tree
from src.dino import Dino
from src.obstacle import Tree, FlyingObstacle
from src.cloud import Cloud
from src.background import background

pygame.init()
pygame.display.set_caption('Jumping dino')
MAX_WIDTH = 800
MAX_HEIGHT = 400
gamespeed = 12
screen = pygame.display.set_mode((MAX_WIDTH, MAX_HEIGHT))

def main():
    # set screen, fps
    fps = pygame.time.Clock()
    run = True
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


if __name__ == '__main__':
    main()