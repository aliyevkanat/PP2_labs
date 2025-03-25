import pygame
import os 

pygame.init()
pygame.mixer.init()
image = pygame.image.load('lab7/player1.png')
screen = pygame.display.set_mode((500,400))
songs = [
    "lab7/Track 1.mp3",
    "lab7/Track 2.mp3"
]
current_song = 0

def playsong(num):
    pygame.mixer.music.load(songs[num])
    pygame.mixer.music.play()

playsong(current_song)

x = 0
y = 0
done = False 
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    screen.fill((0,0,0))
    screen.blit(image, (x,y))

    keys = pygame.key.get_pressed()
    if keys[pygame.K_q]: 
        pygame.mixer.music.pause()
    if keys[pygame.K_w]: 
        pygame.mixer.music.unpause()
    if keys[pygame.K_e]: 
        current_song = (current_song + 1)
        playsong(current_song)
    if keys[pygame.K_r]: 
        current_song = (current_song -1)
        playsong(current_song)

    
    pygame.time.delay(100)
    pygame.display.flip()


pygame.quit()