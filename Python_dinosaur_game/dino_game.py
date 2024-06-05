import pygame
import random
import sys
import os
from src.dino import Dino
from src.obstacle import Cactus, Bird, Trap, manage_obstacles
from src.cloud import Cloud
from src.background import background
from src.lifemanage import LifeManager
from src.levelmanage import LevelManager

pygame.init()
pygame.display.set_caption('Jumping dino')
MAX_WIDTH = 800
MAX_HEIGHT = 400
y_pos_bg = 330
screen = pygame.display.set_mode((MAX_WIDTH, MAX_HEIGHT))

show_hitbox = False

def main():
    global show_hitbox
    
    # 초기 설정
    clock = pygame.time.Clock()
    run_game = True
    game_speed = 12
    death_count = 0

    # 게임 객체 생성
    dino = Dino()
    obstacles = pygame.sprite.Group()
    life_manager = LifeManager()
    level_manager = LevelManager()
    cloud = Cloud()
    
    last_obstacle_time = pygame.time.get_ticks()
    start_time = pygame.time.get_ticks()

    while run_game:
        run_game = handle_events()
        game_speed = update_game_speed(level_manager)
        
        current_time = pygame.time.get_ticks()
        last_obstacle_time = manage_obstacles(obstacles, last_obstacle_time, current_time)

        update_screen(dino, cloud, obstacles, life_manager, level_manager, start_time)

        if check_collisions(dino, obstacles, life_manager):
            pygame.time.delay(300)
            life_manager.lose_life()
            if not life_manager.is_alive():
                death_count += 1  
                life_manager.reset_lives()  
                menu(death_count)

        pygame.display.update()
        clock.tick(30)

# 이벤트 처리 함수
def handle_events():
    global show_hitbox
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p:
                show_hitbox = not show_hitbox
    return True

# 레벨별 게임속도 증가
def update_game_speed(level_manager):
    base_speed = 12
    return base_speed + level_manager.get_level() * 5

# 화면 업데이트 함수
def update_screen(dino, cloud, obstacles, life_manager, level_manager, start_time):
    screen.fill((255, 255, 255))
    user_input = pygame.key.get_pressed()

    obstacles.update(update_game_speed(level_manager))
    for obstacle in obstacles:
        obstacle.draw(screen, show_hitbox)

    dino.draw(screen, show_hitbox)
    dino.dinoupdate(user_input)

    cloud.draw(screen)
    cloud.update()

    background()

    life_manager.update_invincibility()

    display_info(life_manager, level_manager, start_time)

# 충돌 확인 함수
def check_collisions(dino, obstacles, life_manager):
    if not life_manager.is_invincible(): 
        for obstacle in obstacles:
            if dino.dino_rect.colliderect(obstacle.rect):
                return True
    return False

# 정보 표시: 잔여생명, 점수, 레벨, 히트박스 온오프
def display_info(life_manager, level_manager, start_time):
    font = pygame.font.Font('freesansbold.ttf', 20)

    lives_text = font.render(f'Life: {life_manager.get_lives()}', True, (0, 0, 0))
    screen.blit(lives_text, (10, 10))

    current_time = pygame.time.get_ticks()
    score = (current_time - start_time) // 100
    score_text = font.render(f'Score: {score}', True, (0, 0, 0))
    score_text_rect = score_text.get_rect(center=(MAX_WIDTH // 2, 30))
    screen.blit(score_text, score_text_rect.topleft)

    level_manager.update_level(score)
    level_text = font.render(f'Lv: {level_manager.get_level()}', True, (0, 0, 0))
    screen.blit(level_text, (10, 40))
    
    hitbox_text = font.render(f'Hitbox: {"ON" if show_hitbox else "OFF"}  push P', True, (0, 0, 0))
    screen.blit(hitbox_text, (10, 70))

def menu(death_count):
    run = True
    base_path = os.path.dirname(__file__)
    while run:
        font = pygame.font.Font('freesansbold.ttf', 30)
        small_font = pygame.font.Font('freesansbold.ttf', 20)
        RunDino = pygame.image.load(os.path.join(base_path, 'images/Dino/DinoRun1.png'))
        GameoverImg = pygame.image.load(os.path.join(base_path, 'images/Other/Gameover.png'))
        ResetImg = pygame.image.load(os.path.join(base_path, 'images/Other/Reset.png'))

        if death_count == 0:
            screen.fill((255, 255, 255))
            text = font.render("Press any Key to Start", True, (0, 0, 0))
            text_rect = text.get_rect(center=(MAX_WIDTH // 2, MAX_HEIGHT // 2))
            screen.blit(text, text_rect)
            screen.blit(RunDino, (MAX_WIDTH // 2 - 20, MAX_HEIGHT // 2 - 140))
        elif death_count > 0:
            screen.fill((255, 255, 255))
            gameover_rect = GameoverImg.get_rect(center=(MAX_WIDTH // 2, MAX_HEIGHT // 2 - 50))
            reset_rect = ResetImg.get_rect(center=(MAX_WIDTH // 2, MAX_HEIGHT // 2 + 50))
            screen.blit(GameoverImg, gameover_rect)
            screen.blit(ResetImg, reset_rect)

            restart_text1 = small_font.render("or", True, (0, 0, 0))
            restart_text2 = small_font.render("Press any Key to RESTART", True, (0, 0, 0))
            restart_text1_rect = restart_text1.get_rect(center=(MAX_WIDTH // 2, MAX_HEIGHT // 2 + 100))
            restart_text2_rect = restart_text2.get_rect(center=(MAX_WIDTH // 2, MAX_HEIGHT // 2 + 130))
            screen.blit(restart_text1, restart_text1_rect.topleft)
            screen.blit(restart_text2, restart_text2_rect.topleft)

        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit(1)
            if event.type == pygame.KEYDOWN:
                main()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if death_count > 0 and reset_rect is not None and reset_rect.collidepoint(event.pos):
                    main()

menu(death_count=0)