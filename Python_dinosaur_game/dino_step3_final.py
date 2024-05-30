# python game with pygame : Jumping dino
# by. BlockDMask
import pygame
import sys
from src.obstacle import Tree
from src.dino import Dino

# step1 : set screen, fps
# step2 : show dino, jump dino
# step3 : show tree, move tree

pygame.init()
pygame.display.set_caption('Jumping dino')
MAX_WIDTH = 800
MAX_HEIGHT = 400


def main():
    # set screen, fps
    screen = pygame.display.set_mode((MAX_WIDTH, MAX_HEIGHT))
    fps = pygame.time.Clock()
    run = True

    # dino
    dino = Dino()

    # tree
    tree = Tree(screen, 'Python_dinosaur_game/images/tree.png', MAX_WIDTH, MAX_HEIGHT)

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

        # draw dino
        dino.draw(screen)
        dino.dinoupdate(userinput)
        # update
        pygame.display.update()
        fps.tick(30)


if __name__ == '__main__':
    main()