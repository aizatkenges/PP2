import pygame
import sys


pygame.init()


screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Moving Ball")

WHITE = (255, 255, 255)
RED = (255, 0, 0)

ball_radius = 25
ball_x = (screen_width - ball_radius * 2) // 2
ball_y = (screen_height - ball_radius * 2) // 2
ball_speed = 20

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                if ball_y - ball_speed >= 0:
                    ball_y -= ball_speed
            elif event.key == pygame.K_DOWN:
                if ball_y + ball_speed <= screen_height - ball_radius * 2:
                    ball_y += ball_speed
            elif event.key == pygame.K_LEFT:
                if ball_x - ball_speed >= 0:
                    ball_x -= ball_speed
            elif event.key == pygame.K_RIGHT:
                if ball_x + ball_speed <= screen_width - ball_radius * 2:
                    ball_x += ball_speed

    
    screen.fill(WHITE)

    
    pygame.draw.circle(screen, RED, (ball_x + ball_radius, ball_y + ball_radius), ball_radius)

    
    pygame.display.flip()

    
    pygame.time.Clock().tick(30)


pygame.quit()
sys.exit()
