import pygame
import sys
import random

pygame.init() # Инициализация

width, height = 800, 600 # screen setup
c_size = 20 # size of one cell

# Colors
white = (255, 255, 255)
red = (255, 0, 0)
black = (0, 0, 0)
green = (0, 255, 0)

# Creating a window
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Snake")

# Шрифты
font_big = pygame.font.SysFont("Arial", 60)
font_small = pygame.font.SysFont("Arial", 30)

class Snake:
    def __init__(self):
        self.body = [(100, 60), (80, 60), (60, 60)]
        self.direction = "RIGHT"

    def move(self):
        head_x, head_y = self.body[0]
        if self.direction == "RIGHT":
            head_x += c_size
        elif self.direction == "LEFT":
            head_x -= c_size
        elif self.direction == "UP":
            head_y -= c_size
        elif self.direction == "DOWN":
            head_y += c_size

        head_x %= width
        head_y %= height

        new_head = (head_x, head_y)

        if new_head in self.body[1:]:
            return False

        self.body.insert(0, new_head)
        return True

    def grow(self):
        pass

    def draw(self, surface):
        for segment in self.body:
            pygame.draw.rect(surface, green, (segment[0], segment[1], c_size, c_size))

class Food:
    def __init__(self, snake_body):
        self.spawn(snake_body)

    def spawn(self, snake_body):
        while True:
            self.x = random.randint(0, (width - c_size) // c_size) * c_size
            self.y = random.randint(0, (height - c_size) // c_size) * c_size

            if (self.x, self.y) not in snake_body:
                break

        self.weight = random.choice([1, 1, 1, 2, 3])
        self.spawn_time = pygame.time.get_ticks()

    def draw(self, surface):
        if self.weight == 1:
            color = red
        elif self.weight == 2:
            color = (255, 165, 0)
        else:
            color = (0, 0, 255)

        pygame.draw.rect(surface, color, (self.x, self.y, c_size, c_size))

    def disappearing(self, duration = 7000):
        #Food disappears after 7 seconds
        cur_t = pygame.time.get_ticks()
        return cur_t - self.spawn_time > duration

def game():
    clock = pygame.time.Clock()
    snake = Snake()
    food = Food(snake.body)
    score = 0
    level = 1 
    speed = 5
    running = True
    game_over = False
    while running:
        clock.tick(speed)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and snake.direction != "DOWN":
                    snake.direction = "UP"
                elif event.key == pygame.K_DOWN and snake.direction != "UP":
                    snake.direction = "DOWN"
                elif event.key == pygame.K_RIGHT and snake.direction != "LEFT":
                    snake.direction = "RIGHT"
                elif event.key == pygame.K_LEFT and snake.direction != "RIGHT":
                    snake.direction = "LEFT"

        if not game_over:
            alive = snake.move()
            if not alive:
                game_over = True

            # Checking your eating habits
            if snake.body[0] == (food.x, food.y):
                score += food.weight
                for i in range(food.weight):
                    snake.grow()

                food.spawn(snake.body)

                # level up 
                if score // 5 >= level:
                    level += 1
                    speed += 2 # Speed increase

            else:
                snake.body.pop() # normal movement (tail removal)

            # Checking for food disappearing
            if food.disappearing():
                food.spawn(snake.body)

        screen.fill(black)
        snake.draw(screen)
        food.draw(screen)

        # Account and level withdrawal
        score_text = font_small.render(f"Score: {score}", True, white)
        level_text = font_small.render(f"Level: {level}", True, white)
        screen.blit(score_text, (width - 150, 20))
        screen.blit(level_text, (width - 150, 50))

        if game_over:
            over_text = font_big.render("GAME OVER!", True, red)
            screen.blit(over_text, (width // 2 - 180, height // 2 - 30))

        pygame.display.update()

if __name__ == "__main__":
    game()