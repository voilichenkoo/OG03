import pygame
import random

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Игра Тир')

icon = pygame.image.load('img\icon.jpg')
pygame.display.set_icon(icon)

target_image = pygame.image.load('img\target.png')
target_height = 80
target_width = 80
target_x = random.randint(0,SCREEN_WIDTH - target_width)
target_y = random.randint(0,SCREEN_HEIGHT - target_height)

color = (100,100,100)

running_true = True
while running_true:
    screen.fill(color)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if target_x < mouse_x < target_x + target_width and target_y < mouse_y + target_height:
                target_x = random.randint(0, SCREEN_WIDTH - target_width)
                target_y = random.randint(0, SCREEN_HEIGHT - target_height)
    screen.blit(target_image, (target_x,target_y))

pygame.quite()

