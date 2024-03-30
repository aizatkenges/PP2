import pygame
import sys
from datetime import datetime

pygame.init()


screen_width = 400
screen_height = 400
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Mickey Mouse Clock")


mickey_image = pygame.image.load("mickey.png")
mickey_image = pygame.transform.scale(mickey_image, (200, 200))

def draw_clock(seconds_angle, minutes_angle):
    screen.fill((255, 255, 255)) 


    mickey_rect = mickey_image.get_rect(center=(screen_width // 2, screen_height // 2))
    screen.blit(mickey_image, mickey_rect)

    seconds_hand = pygame.Surface((100, 4), pygame.SRCALPHA)
    pygame.draw.rect(seconds_hand, (255, 0, 0), (0, 0, 100, 4))
    seconds_hand_rotated = pygame.transform.rotate(seconds_hand, seconds_angle)
    seconds_hand_rect = seconds_hand_rotated.get_rect(center=mickey_rect.center)
    screen.blit(seconds_hand_rotated, seconds_hand_rect)

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

    current_time = datetime.now()
    seconds = current_time.second
    minutes = current_time.minute

    seconds_angle = -6 * seconds  
    minutes_angle = -6 * (minutes + seconds / 60)  

    # Draw clock
    draw_clock(seconds_angle, minutes_angle)

    clock.tick(60)  

pygame.quit()
sys.exit()
