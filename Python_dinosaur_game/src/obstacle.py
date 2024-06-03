import pygame
import random

# 이미지 경로
BIRD_IMAGE_PATHS = [
    'Python_dinosaur_game/images/Obstacle/Bird/Bird1.png', 
    'Python_dinosaur_game/images/Obstacle/Bird/Bird2.png'
]

CACTUS_IMAGE_PATHS = [
    'Python_dinosaur_game/images/Obstacle/Cactus/LargeCactus1.png', 
    'Python_dinosaur_game/images/Obstacle/Cactus/LargeCactus2.png', 
    'Python_dinosaur_game/images/Obstacle/Cactus/LargeCactus3.png', 
    'Python_dinosaur_game/images/Obstacle/Cactus/SmallCactus1.png', 
    'Python_dinosaur_game/images/Obstacle/Cactus/SmallCactus2.png', 
    'Python_dinosaur_game/images/Obstacle/Cactus/SmallCactus3.png'
]

TRAP_IMAGE_PATH = 'Python_dinosaur_game/images/Obstacle/Trap.png'

y_pos_bg = 330 # src/background.py의 Track에 대한 높이

class Obstacle(pygame.sprite.Sprite):
    def __init__(self, image_path, x_pos, y_pos, speed):
        super().__init__()
        self.image = pygame.image.load(image_path) 
        self.rect = self.image.get_rect(topleft=(x_pos, y_pos)) # 이미지 좌표설정 및 충돌영역 초기화
        self.speed = speed

    def update(self):
        self.rect.x -= self.speed # 왼쪽으로 진행
        if self.rect.right < 0:  # 화면 왼쪽으로 완전히 사라지면
            self.kill() # 장애물을 스프라이트 그룹에서 제거

class Cactus(Obstacle):
    def __init__(self):
        image_path = random.choice(CACTUS_IMAGE_PATHS) # 선인장 이미지 랜덤 선택
        image = pygame.image.load(image_path)
        y_pos = y_pos_bg - image.get_rect().height + 10 # + 10은 Track.png의 공백에 대한 보정
        super().__init__(image_path, 800, y_pos, 12)

class Bird(Obstacle):
    def __init__(self):
        self.image_paths = BIRD_IMAGE_PATHS  # 이미지 경로 목록
        self.current_image_index = 0  # 현재 이미지 인덱스
        image_path = self.image_paths[self.current_image_index]  # 초기 이미지 경로
        image = pygame.image.load(image_path)
        y_pos = random.randint(200, y_pos_bg - image.get_rect().height)
        super().__init__(image_path, 800, y_pos, 17)
        self.animation_time = 0  # 애니메이션 시간 초기화

    def update(self):
        self.animation_time += 1
        if self.animation_time % 5 == 0:  # 이미지 교체 속도 조절
            self.current_image_index = (self.current_image_index + 1) % len(self.image_paths)
            self.image = pygame.image.load(self.image_paths[self.current_image_index])
        super().update()  # 부모 클래스의 update 메서드 호출
        
class Trap(Obstacle):
    def __init__(self):
        image_path = TRAP_IMAGE_PATH
        y_pos = y_pos_bg +5 # +5는 트랩의 높이 보정
        super().__init__(image_path, 800, y_pos, 12)

def manage_obstacles(obstacles_group, last_obstacle_time, current_time):
    if current_time - last_obstacle_time > random.randint(1500, 3000): # 장애물 생성 텀
        obstacle_type = random.choice([Cactus, Bird, Trap])()
        obstacles_group.add(obstacle_type)
        return current_time
    return last_obstacle_time