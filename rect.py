import sys
import pygame


pygame.init()
fill_color = (32, 52, 71)
screen_width = 800
screen_height = 600

screen = pygame.display.set_mode((screen_width, screen_height))
rect_wigth, rect_height = 100, 200
rect_x = screen_width / 2 - rect_wigth / 2
rect_y = screen_height / 2 - rect_height / 2
rect_color = pygame.Color('lightyellow')

STEP = 10

pygame.display.set_caption("My game")

while True:
    for event in pygame.event.get():
        # print(event)
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and rect_y >= STEP:
                rect_y -= STEP
            if event.key == pygame.K_DOWN and rect_y <= screen_height - rect_height - STEP:
                rect_y += STEP
            if event.key == pygame.K_LEFT and rect_x >= STEP:
                rect_x -= STEP
            if event.key == pygame.K_RIGHT and rect_x <= screen_width - rect_wigth - STEP:
                rect_x += STEP

    screen.fill(fill_color)
    pygame.draw.rect(screen, rect_color, (rect_x, rect_y, rect_wigth, rect_height))
    pygame.display.update()