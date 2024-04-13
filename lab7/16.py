import pygame
import sys


pygame.init()


WINDOW_WIDTH, WINDOW_HEIGHT = 800, 600
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Moving Ball")

WHITE = (255, 255, 255)
RED = (255, 0, 0)


radius = 25



while True:
    window.fill(WHITE)  

   
    pygame.draw.circle(window, RED, (50, 50), radius)

    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            
            if event.key == pygame.K_UP:
                y = max(y - 20, radius)  
            elif event.key == pygame.K_DOWN:
                y = min(y + 20, WINDOW_HEIGHT - radius)  
            elif event.key == pygame.K_LEFT:
                x = max(x - 20, radius)  
            elif event.key == pygame.K_RIGHT:
                x = min(x + 20, WINDOW_WIDTH - radius)  

   
    pygame.display.update()
