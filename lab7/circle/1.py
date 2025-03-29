import pygame
pygame.init()

# Window settings
window_size = (800, 600)
screen = pygame.display.set_mode(window_size)
pygame.display.set_caption("Draw circle")

# Colors
ball_color = pygame.Color('red')
bg_color = pygame.Color('white')

# Ball settings
ball_pos = [400, 300]  # Initial position
ball_radius = 25  # Radius
speed = 19  # Movement speed

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    
    # Movement controls
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        ball_pos[1] = max(ball_pos[1] - speed, ball_radius)
    if keys[pygame.K_DOWN]:
        ball_pos[1] = min(ball_pos[1] + speed, window_size[1] - ball_radius)
    if keys[pygame.K_LEFT]:
        ball_pos[0] = max(ball_pos[0] - speed, ball_radius)
    if keys[pygame.K_RIGHT]:
        ball_pos[0] = min(ball_pos[0] + speed, window_size[0] - ball_radius)
    
    # Draw ball
    screen.fill(bg_color)
    pygame.draw.circle(screen, ball_color, ball_pos, ball_radius)
    pygame.display.flip()
    pygame.time.Clock().tick(24)
