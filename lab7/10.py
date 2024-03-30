import pygame
import os


pygame.init()

screen_width = 400
screen_height = 200
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Simple Music Player")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Fonts
font = pygame.font.Font(None, 36)

# Load music files
music_files = ["music1.mp3", "music2.mp3", "music3.mp3"] 
current_music_index = 0


def play_music(file):
    pygame.mixer.music.load(file)
    pygame.mixer.music.play()

def stop_music():
    pygame.mixer.music.stop()


def next_song():
    global current_music_index
    current_music_index = (current_music_index + 1) % len(music_files)
    play_music(music_files[current_music_index])


def previous_song():
    global current_music_index
    current_music_index = (current_music_index - 1) % len(music_files)
    play_music(music_files[current_music_index])


play_music(music_files[current_music_index])


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:  # Play/Pause music on spacebar press
                if pygame.mixer.music.get_busy():
                    stop_music()
                else:
                    play_music(music_files[current_music_index])
            elif event.key == pygame.K_RIGHT:  # Play next song on right arrow key press
                next_song()
            elif event.key == pygame.K_LEFT:  # Play previous song on left arrow key press
                previous_song()

    # Draw text on the screen
    screen.fill(WHITE)
    text_play_pause = font.render("Spacebar: Play/Pause", True, BLACK)
    text_next = font.render("Right Arrow: Next Song", True, BLACK)
    text_previous = font.render("Left Arrow: Previous Song", True, BLACK)
    screen.blit(text_play_pause, (20, 20))
    screen.blit(text_next, (20, 60))
    screen.blit(text_previous, (20, 100))

    pygame.display.flip()

pygame.quit()
