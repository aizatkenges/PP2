import pygame
import sys
from datetime import datetime

# Initialize Pygame
pygame.init()

# Set up the screen
screen_width = 400
screen_height = 400
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Mickey Mouse Clock")

# Load Mickey Mouse image
mickey_image = pygame.image.load("mickey.png")
mickey_image = pygame.transform.scale(mickey_image, (200, 200))

def draw_clock(seconds_angle, minutes_angle):
    screen.fill((255, 255, 255))  # Fill the screen with white

    # Draw Mickey Mouse image
    mickey_rect = mickey_image.get_rect(center=(screen_width // 2, screen_height // 2))
    screen.blit(mickey_image, mickey_rect)

    # Draw seconds hand
    seconds_hand = pygame.Surface((100, 4), pygame.SRCALPHA)
    pygame.draw.rect(seconds_hand, (255, 0, 0), (0, 0, 100, 4))
    seconds_hand_rotated = pygame.transform.rotate(seconds_hand, seconds_angle)
    seconds_hand_rect = seconds_hand_rotated.get_rect(center=mickey_rect.center)
    screen.blit(seconds_hand_rotated, seconds_hand_rect)

    # Draw minutes hand
    minutes_hand = pygame.Surface((80, 4), pygame.SRCALPHA)
    pygame.draw.rect(minutes_hand, (0, 0, 255), (0, 0, 80, 4))
    minutes_hand_rotated = pygame.transform.rotate(minutes_hand, minutes_angle)
    minutes_hand_rect = minutes_hand_rotated.get_rect(center=mickey_rect.center)
    screen.blit(minutes_hand_rotated, minutes_hand_rect)

    pygame.display.flip()

clock = pygame.time.Clock()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Get current time
    current_time = datetime.now()
    seconds = current_time.second
    minutes = current_time.minute

    # Calculate angles for hands
    seconds_angle = -6 * seconds  # Each second corresponds to 6 degrees rotation
    minutes_angle = -6 * (minutes + seconds / 60)  # Each minute corresponds to 6 degrees rotation

    # Draw clock
    draw_clock(seconds_angle, minutes_angle)

    clock.tick(60)  # Limit to 60 frames per second

pygame.quit()
sys.exit()
