import pygame
import sys
import random
import psycopg2

pygame.init()

# Screen setup
width, height = 800, 600
c_size = 20

# Colors
white = (255, 255, 255)
red = (255, 0, 0)
black = (0, 0, 0)
green = (0, 255, 0)

# Screen
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Snake Game")

# Fonts
font_big = pygame.font.SysFont("Arial", 60)
font_small = pygame.font.SysFont("Arial", 30)

# --- SQL FUNCTIONS ---

def insert_score(name, score, level):
    conn = psycopg2.connect(dbname='lab10', user='postgres', password='Aa1234', host='localhost', port='5432')
    cur = conn.cursor()
    insert_query = "INSERT INTO snake_game_scores (player_name, score, level) VALUES (%s, %s, %s)"
    cur.execute(insert_query, (name, score, level))
    conn.commit()
    cur.close()
    conn.close()

def get_scores(name):
    conn = psycopg2.connect(dbname='lab10', user='postgres', password='Aa1234', host='localhost', port='5432')
    cur = conn.cursor()
    query = "SELECT score, level FROM snake_game_scores WHERE player_name = %s ORDER BY score DESC"
    cur.execute(query, (name,))
    results = cur.fetchall()
    cur.close()
    conn.close()
    return results

# --- CLASSES ---

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

        # Столкновение с границами
        if head_x < 0 or head_x >= width or head_y < 0 or head_y >= height:
            return False

        new_head = (head_x, head_y)
        if new_head in self.body[1:]:  # Столкновение с собой
            return False

        self.body.insert(0, new_head)
        return True

    def grow(self):
        # Ничего не делать, потому что хвост не удаляется при поедании
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

    def disappearing(self, duration=7000):
        return pygame.time.get_ticks() - self.spawn_time > duration

# --- MAIN GAME LOOP ---

def game():
    player_name = input("Enter your name: ")
    player_name = player_name.encode('utf-8', 'ignore').decode('utf-8')

    scores = get_scores(player_name)
    if scores:
        print("Your previous scores:")
        for s, l in scores:
            print(f"Score: {s}, Level: {l}")
        input("Press Enter to play a new game...")

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
                insert_score(player_name, score, level)
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
                insert_score(player_name, score, level)
                game_over = True

            if snake.body[0] == (food.x, food.y):
                score += food.weight
                for _ in range(food.weight):
                    snake.grow()
                food.spawn(snake.body)

                if score // 5 >= level:
                    level += 1
                    speed += 1

            else:
                snake.body.pop()

            if food.disappearing():
                food.spawn(snake.body)

        # Drawing
        screen.fill(black)
        snake.draw(screen)
        food.draw(screen)

        score_text = font_small.render(f"Score: {score}  Level: {level}", True, white)
        screen.blit(score_text, (10, 10))

        if game_over:
            over_text = font_big.render("Game Over", True, red)
            screen.blit(over_text, (width // 2 - 150, height // 2 - 30))

        pygame.display.flip()

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    game()
