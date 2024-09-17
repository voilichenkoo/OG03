import pygame
import random
import time

pygame.init()

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 400

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Игра Тир')

icon = pygame.image.load('img/icon.jpg')
pygame.display.set_icon(icon)

target_image = pygame.image.load('img/my_target.png')
target_height = 57
target_width = 80

# Начальные координаты цели
target_x = random.randint(0, SCREEN_WIDTH - target_width)
target_y = random.randint(0, SCREEN_HEIGHT - target_height)

# Скорость движения цели
target_speed_x = random.choice([-3, 3])  # Случайное направление по X
target_speed_y = random.choice([-3, 3])  # Случайное направление по Y

background_color = (0, 0, 255)

# Переменные для подсчета очков
score = 0
font = pygame.font.Font(None, 36)

running_true = True
while running_true:
    screen.fill(background_color)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running_true = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            # Проверка попадания по цели
            if target_x < mouse_x < target_x + target_width and target_y < mouse_y < target_y + target_height:
                score += 1  # Увеличиваем счет
                # Перемещаем цель в случайное место
                target_x = random.randint(0, SCREEN_WIDTH - target_width)
                target_y = random.randint(0, SCREEN_HEIGHT - target_height)
                target_speed_x = random.randint(-3, 3)  # Случайное направление по X
                target_speed_y = random.randint(-3, 3)  # Случайное направление по Y
                print(target_speed_x,' ', target_speed_y)

    # Обновляем координаты цели
    target_x += target_speed_x
    target_y += target_speed_y

    # Проверяем границы экрана и меняем направление
    if target_x <= 0 or target_x >= SCREEN_WIDTH - target_width:
        target_speed_x *= -1  # Меняем направление по X
    if target_y <= 0 or target_y >= SCREEN_HEIGHT - target_height:
        target_speed_y *= -1  # Меняем направление по Y

    # Отображаем цель
    screen.blit(target_image, (target_x, target_y))

    # Отображаем счет на экране
    score_text = font.render(f'Очки: {score}', True, (255, 255, 255))
    screen.blit(score_text, (10, 10))
    time.sleep(.02)

    pygame.display.update()

pygame.quit()
