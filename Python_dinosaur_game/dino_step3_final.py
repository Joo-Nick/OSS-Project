import pygame
import random
import sys
import os
from src.dino import Dino
from src.obstacle import Cactus, Bird, manage_obstacles
from src.obstacle_random import Trap
from src.cloud import Cloud
from src.background import background

pygame.init()
pygame.display.set_caption('Jumping dino')
MAX_WIDTH = 800
MAX_HEIGHT = 400
y_pos_bg = 330
screen = pygame.display.set_mode((MAX_WIDTH, MAX_HEIGHT))

def main():
    # 변수 설정
    fps = pygame.time.Clock()
    run = True
    gamespeed = 12
    death_count = 0
    trap_spawn_time = random.randint(1000, 5000)  # 1초에서 5초 사이의 랜덤 시간 간격 (변경 가능)
    last_trap_spawn = pygame.time.get_ticks()

    # dino 인스턴스 생성
    dino = Dino()

    # 장애물 그룹 생성
    obstacles = pygame.sprite.Group()

    # 시간 추적을 위한 변수
    last_obstacle_time = pygame.time.get_ticks()

    # 현재 파일의 디렉토리 경로 가져오기
    base_path = os.path.dirname(__file__)

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
                run = False

        # management obsacle
        current_time = pygame.time.get_ticks()
        last_obstacle_time = manage_obstacles(obstacles, last_obstacle_time, current_time)

        obstacles.update()
        obstacles.draw(screen)
        
        # 현재 시간 체크
        current_time = pygame.time.get_ticks()
        
        # trap 생성
        if current_time - last_trap_spawn > trap_spawn_time:
            new_trap = Trap(screen, 'Python_dinosaur_game/images/Obstacle/Trap.png')
            traps.append(new_trap)
            last_trap_spawn = current_time
            trap_spawn_time = random.randint(1000, 5000)  # 다음 트랩 생성 시간 갱신

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
        for obstacle in obstacles:
            if dino.dino_rect.colliderect(obstacle.rect):
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