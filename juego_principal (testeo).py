import pygame
from clases.pyvidplayer import Video
import sys

pygame.init()
win = pygame.display.set_mode((800,500))
clock = pygame.time.Clock()

#provide video class with the path to your video
vid = Video("recursos/videos/introduccion.mov")
vid.set_size((800,500))
print(vid.frame_count)
contador = vid.frame_count

while True:
    vid.draw(win, (0, 0), False)
    print(vid.active)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        elif event.type == pygame.KEYDOWN:
            key = pygame.key.name(event.key)
            if key == "r":
                vid.restart()           #rewind video to beginning
            elif key == "p":
                vid.toggle_pause()      #pause/plays video
            elif key == "right":
                vid.seek(15)            #skip 15 seconds in video
            elif key == "left":
                vid.seek(-15)           #rewind 15 seconds in video
            elif key == "up":
                vid.set_volume(1.0)     #max volume
            elif key == "down":
                vid.set_volume(0.0)     #min volume
            #your program frame rate does not affect video playback
            clock.tick(60)
    #draws the video to the given surface, at the given position
    pygame.display.update()