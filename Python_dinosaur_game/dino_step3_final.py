import pygame
import random
import sys
import os
from src.dino import Dino
from src.obstacle import Tree, FlyingObstacle
from src.obstacle_random import Trap
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
    death_count = 0
    trap_spawn_time = random.randint(2000, 5000)  # 2초에서 5초 사이의 랜덤 시간 간격
    last_trap_spawn = pygame.time.get_ticks()

    # dino 인스턴스 생성
    dino = Dino()

    # 현재 파일의 디렉토리 경로 가져오기
    base_path = os.path.dirname(__file__)

    # tree 인스턴스 생성
    tree = Tree(screen, os.path.join(base_path, 'images/Obstacle/Tree.png'))

    # flying_obstacle 인스턴스 생성
    flying_obstacle = FlyingObstacle(screen, os.path.join(base_path, 'images/Obstacle/FlyingObstacle.png'))

    # trap 리스트 생성
    traps = []
    
    # Cloud 인스턴스 생성
    cloud = Cloud()

    while run:
        screen.fill((255, 255, 255))
        userinput = pygame.key.get_pressed()

        # event check
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit(1)
                
        # tree move
        tree.move()

        # draw tree
        tree.draw()

        # flying obstacle move
        flying_obstacle.move()

        # draw flying obstacle
        flying_obstacle.draw()
        
        # 현재 시간 체크
        current_time = pygame.time.get_ticks()
        
        # trap 생성
        if current_time - last_trap_spawn > trap_spawn_time:
            new_trap = Trap(screen, 'Python_dinosaur_game/images/Obstacle/Trap.png')
            traps.append(new_trap)
            new_trap.set_tree_x(tree.x)  # 나무의 x 좌표 설정
            new_trap.x = new_trap.generate_random_x()  # 랜덤한 x 좌표 생성
            last_trap_spawn = current_time
            trap_spawn_time = random.randint(2000, 5000)  # 다음 트랩 생성 시간 갱신

        # trap move and draw
        for trap in traps[:]:
            if not trap.move_random():
                traps.remove(trap)
            else:
                trap.draw_random()
                
        # draw dino
        dino.draw(screen)
        dino.dinoupdate(userinput)

        # draw cloud
        cloud.draw(screen)
        cloud.update()

        # background
        background()

        # 충돌 조건문
        if dino.dino_rect.colliderect(tree.rect) or any(dino.dino_rect.colliderect(trap.rect) for trap in traps):
            pygame.time.delay(300)
            dino.dino_run = False
            dino.dino_jump = False
            dino.dino_duck = False
            dino.dino_dead = True
            death_count += 1
            menu(death_count)

        # update
        pygame.display.update()
        fps.tick(30)

def menu(death_count):
    run = True
    base_path = os.path.dirname(__file__)
    while run:
        font = pygame.font.Font('freesansbold.ttf', 30)
        RunDino = pygame.image.load(os.path.join(base_path, 'images/Dino/DinoRun1.png'))
        GameoverImg = pygame.image.load(os.path.join(base_path, 'images/Other/Gameover.png'))
        ResetImg = pygame.image.load(os.path.join(base_path, 'images/Other/Reset.png'))

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
            screen.blit(ResetImg, resetRect)

        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit(1)
            if event.type == pygame.KEYDOWN:
                main()

menu(death_count=0)
