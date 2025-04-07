import pygame
import sys
import random

# Инициализация
pygame.init()

# Константы
we = 600
he = 800
FPS = 60
N = 5

screen = pygame.display.set_mode((we, he))
pygame.display.set_caption("Racer")

clock = pygame.time.Clock()

# Загрузка фона
background = pygame.image.load("background.png")
background = pygame.transform.scale(background, (we, he))

# Загрузка изображений
car = pygame.image.load("car.png")
car = pygame.transform.scale(car, (140, 70))
car = pygame.transform.rotate(car, -90)

enemy = pygame.image.load("enemy.png")
enemy = pygame.transform.scale(enemy, (140, 70))
enemy = pygame.transform.rotate(enemy, 90)

coin_img = pygame.image.load("coin.png")
coin_img = pygame.transform.scale(coin_img, (50, 50))

# Параметры машины
car_x = we // 2 - 30
car_y = he - 150
speed = 7

# Параметры врага
enemy_x = random.randint(50, we - 140 - 50)
enemy_y = -100
enemy_speed = 3

# Монеты
coin_weights = [1, 2, 3, 5]
coins = []

# Шрифты
score_font = pygame.font.SysFont("Arial", 30)
font = pygame.font.SysFont("Arial", 60)

coin_cnt = 0
game_over = False

# Функция создания монеты
def spawn_coin():
    weight = random.choice(coin_weights)
    coin_x = random.randint(50, we - 100)
    coin_y = -random.randint(100, 500)
    speed = random.randint(3, 5)
    return {"x": coin_x, "y": coin_y, "weight": weight, "speed": speed}

for _ in range(5):
    coins.append(spawn_coin())

# Игровой цикл
running = True
while running:
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if not game_over:
        # Управление машиной
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and car_x > 0:
            car_x -= speed
        if keys[pygame.K_RIGHT] and car_x < we - 60:
            car_x += speed
        if keys[pygame.K_UP] and car_y > 0:
            car_y -= speed
        if keys[pygame.K_DOWN] and car_y < he - 120:
            car_y += speed

        # Движение врага
        enemy_y += enemy_speed
        if enemy_y > he:
            enemy_y = -100
            enemy_x = random.randint(50, we - 140 - 50)

        # Движение монет
        for c in coins:
            c["y"] += c["speed"]
            if c["y"] > he:
                coins.remove(c)
                coins.append(spawn_coin())

        # Проверка столкновений
        car_rect = pygame.Rect(car_x + 10, car_y + 10, car.get_width() - 20, car.get_height() - 10)
        enemy_rect = pygame.Rect(enemy_x + 10, enemy_y + 10, enemy.get_width() - 20, enemy.get_height() - 10)

        # Столкновения с монетами
        for c in coins[:]:
            coin_rect = pygame.Rect(c["x"], c["y"], coin_img.get_width(), coin_img.get_height())
            if car_rect.colliderect(coin_rect):
                coin_cnt += c["weight"]
                coins.remove(c)
                coins.append(spawn_coin())

                # Увеличение скорости врага за каждые N очков
                if coin_cnt % N == 0:
                    enemy_speed += 1

        # Столкновение с врагом
        if car_rect.colliderect(enemy_rect):
            game_over = True

    # Отрисовка
    screen.blit(background, (0, 0))  # Фон

    screen.blit(car, (car_x, car_y))
    screen.blit(enemy, (enemy_x, enemy_y))

    for c in coins:
        screen.blit(coin_img, (c["x"], c["y"]))

    # Отображение счета
    score = score_font.render(f"Coins: {coin_cnt}", True, (255, 0, 0))
    screen.blit(score, (we - 180, 20))

    if game_over:
        text = font.render("Game Over!", True, (255, 0, 0))
        screen.blit(text, (we // 2 - text.get_width() // 2, he // 2 - text.get_height() // 2))

    pygame.display.flip()

# Завершение
pygame.quit()
sys.exit()
