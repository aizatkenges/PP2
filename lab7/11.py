import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the screen
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Moving Ball")

# Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Ball parameters
ball_radius = 25
ball_x = (screen_width - ball_radius * 2) // 2
ball_y = (screen_height - ball_radius * 2) // 2
ball_speed = 20

# Main loop
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

    # Clear the screen
    screen.fill(WHITE)

    # Draw the ball
    pygame.draw.circle(screen, RED, (ball_x + ball_radius, ball_y + ball_radius), ball_radius)

    # Update the display
    pygame.display.flip()

    # Control the frame rate
    pygame.time.Clock().tick(30)

# Quit Pygame
pygame.quit()
sys.exit()
