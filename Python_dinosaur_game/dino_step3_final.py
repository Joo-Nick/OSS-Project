import pygame
import random
import sys
import os
from src.dino import Dino
from src.obstacle import Cactus, Bird, Trap, manage_obstacles
from src.cloud import Cloud
from src.background import background
from src.lifemanage import LifeManager  # LifeManager 클래스 추가

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

    # dino 인스턴스 생성
    dino = Dino()

    # 장애물 그룹 생성
    obstacles = pygame.sprite.Group()
    
    # 목숨 관리자 인스턴스 생성
    lifemanage = LifeManager()

    # 시간 추적을 위한 변수
    last_obstacle_time = pygame.time.get_ticks()

    # 현재 파일의 디렉토리 경로 가져오기
    base_path = os.path.dirname(__file__)

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
        
        # draw dino
        dino.draw(screen)
        dino.dinoupdate(userinput)

        # draw cloud
        cloud.draw(screen)
        cloud.update()

        # background
        background()
        
        # 무적 상태 업데이트
        lifemanage.update_invincibility()  # 수정

        # 충돌 조건문
        if not lifemanage.is_invincible():  # 수정: 무적 상태가 아닐 때만 충돌 체크
            for obstacle in obstacles:
                if dino.dino_rect.colliderect(obstacle.rect):
                    pygame.time.delay(300)
                    lifemanage.lose_life()
                    if not lifemanage.is_alive():
                        death_count += 1  # 수정
                        lifemanage.reset_lives()  # 수정
                        menu(death_count)  # 수정
                    break  # 충돌 후 게임은 계속 진행되며 목숨만 줄어듦 # 수정


                
        # 목숨 정보 표시
        font = pygame.font.Font('freesansbold.ttf', 20)
        lives_text = font.render(f'Life: {lifemanage.get_lives()}', True, (0, 0, 0))
        screen.blit(lives_text, (10, 10))

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
            screen.fill((255, 255, 255))  # 수정: 게임오버 화면 초기화
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