import pygame
import os

pygame.init()


WINDOW_SIZE = (800, 600)
window = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption("Music Player")


music_files = ["music1.mp3", "music2.mp3", "music3.mp3"]
current_track_index = 0
pygame.mixer.music.load(music_files[current_track_index])


def play_music():
    pygame.mixer.music.play()

def stop_music():
    pygame.mixer.music.stop()

def next_track():
    global current_track_index
    current_track_index = (current_track_index + 1) % len(music_files)
    pygame.mixer.music.load(music_files[current_track_index])
    pygame.mixer.music.play()

def previous_track():
    global current_track_index
    current_track_index = (current_track_index - 1) % len(music_files)
    pygame.mixer.music.load(music_files[current_track_index])
    pygame.mixer.music.play()


run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                play_music()
            elif event.key == pygame.K_s:
                stop_music()
            elif event.key == pygame.K_n:
                next_track()
            elif event.key == pygame.K_p:
                previous_track()

    pygame.display.update()

pygame.quit()
