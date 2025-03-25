import pygame 
import time

pygame.init()

screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()
pygame.display.set_caption("Mickey Clock")

image = pygame.image.load("clock.png")
image = pygame.transform.scale(image, (700, 600))

minute_img = pygame.image.load("rightarm.png")
minute_img = pygame.transform.scale(minute_img, (900, 740)) 
second_img = pygame.image.load("leftarm.png")
second_img = pygame.transform.scale(second_img, (65, 540)) 


done = False

while not done: 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    current_time = time.localtime()
    minute = current_time.tm_min
    second = current_time.tm_sec
    
    minute_angle = 360 - (minute * 6 + second / 10)  
    second_angle = 360 - (second * 6)

    screen.fill((255, 255, 255))
    screen.blit(image, (100, 0))
    
    rotated_minute = pygame.transform.rotate(minute_img, minute_angle)
    rotated_second = pygame.transform.rotate(second_img, second_angle)

    minute_rect = rotated_minute.get_rect(center=(450, 300))
    second_rect = rotated_second.get_rect(center=(450, 300))

    screen.blit(rotated_minute, minute_rect)
    screen.blit(rotated_second, second_rect)
    
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
