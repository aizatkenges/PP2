import pygame

# Initialize Pygame
pygame.init()

# Set up the display
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Paint")

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Load images for drawing tools
pencil_img = pygame.image.load("pencil.png")
eraser_img = pygame.image.load("eraser.png")
fill_img = pygame.image.load("fill.png")

# Define drawing tools
PEN = "pen"
ERASER = "eraser"
FILL = "fill"

# Set the initial drawing tool
current_tool = PEN
current_color = BLACK

# Function to draw rectangle
def draw_rectangle(surface, color, start_pos, end_pos):
    pygame.draw.rect(surface, color, (start_pos, (end_pos[0] - start_pos[0], end_pos[1] - start_pos[1])))

# Function to draw circle
def draw_circle(surface, color, center, radius):
    pygame.draw.circle(surface, color, center, radius)

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # Left mouse button
                if current_tool == ERASER:
                    pygame.draw.circle(screen, WHITE, pygame.mouse.get_pos(), 20)
            elif event.button == 3:  # Right mouse button
                current_tool = PEN
            elif event.button == 4:  # Scroll up
                current_color = BLACK
            elif event.button == 5:  # Scroll down
                current_color = WHITE

    screen.fill(WHITE)

    # Draw images for drawing tools
    screen.blit(pencil_img, (50, 10))
    screen.blit(eraser_img, (120, 10))
    screen.blit(fill_img, (190, 10))

    # Draw shapes based on selected tool
    if current_tool == ERASER and pygame.mouse.get_pressed()[0]:
        pygame.draw.circle(screen, WHITE, pygame.mouse.get_pos(), 20)

    pygame.display.flip()

# Quit Pygame
pygame.quit()
