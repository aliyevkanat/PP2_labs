import pygame
import sys

pygame.init()

# Окно
WIDTH, HEIGHT = 1000, 700
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Paint")

# Цвета
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)
COLORS = [BLACK, RED, GREEN, BLUE, WHITE]

# Шрифты
font = pygame.font.SysFont(None, 24)

# Состояния
current_tool = "PENCIL"
current_color = BLACK
text_color = BLACK  # постоянный цвет текста
drawing = False
start_pos = None

def draw_ui():
    instructions = [
        "Инструменты: [P] Карандаш, [E] Ластик, [R] Прямоугольник, [S] Квадрат, [C] Окружность,",
        "[T] Прям. треугольник, [V] Равностор. треугольник, [H] Ромб",
        "Цвета: [1] Чёрный, [2] Красный, [3] Зелёный, [4] Синий, [5] Белый",
        f"Текущий инструмент: {current_tool}",
        f"Текущий цвет: {current_color}"
    ]
    y = 5
    for line in instructions:
        text_surface = font.render(line, True, text_color)
        screen.blit(text_surface, (10, y))
        y += 22

def draw_shape(tool, start, end, color):
    x1, y1 = start
    x2, y2 = end
    w = x2 - x1
    h = y2 - y1

    if tool == "RECT":
        pygame.draw.rect(screen, color, (x1, y1, w, h), 2)
    elif tool == "SQUARE":
        side = min(abs(w), abs(h))
        pygame.draw.rect(screen, color, (x1, y1, side * (1 if w >= 0 else -1), side * (1 if h >= 0 else -1)), 2)
    elif tool == "CIRCLE":
        radius = int(((w)**2 + (h)**2)**0.5 / 2)
        center = ((x1 + x2)//2, (y1 + y2)//2)
        pygame.draw.circle(screen, color, center, radius, 2)
    elif tool == "TRIANGLE":
        points = [start, (x1, y2), (x2, y2)]
        pygame.draw.polygon(screen, color, points, 2)
    elif tool == "EQ_TRIANGLE":
        mid_x = (x1 + x2) // 2
        points = [(mid_x, y1), (x1, y2), (x2, y2)]
        pygame.draw.polygon(screen, color, points, 2)
    elif tool == "RHOMBUS":
        mid_x = (x1 + x2) // 2
        mid_y = (y1 + y2) // 2
        points = [(mid_x, y1), (x2, mid_y), (mid_x, y2), (x1, mid_y)]
        pygame.draw.polygon(screen, color, points, 2)

# Главный цикл
screen.fill(WHITE)
while True:
    draw_ui()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        # Начало рисования
        elif event.type == pygame.MOUSEBUTTONDOWN:
            drawing = True
            start_pos = event.pos
            if current_tool in ["PENCIL", "ERASER"]:
                pygame.draw.circle(screen, WHITE if current_tool == "ERASER" else current_color, event.pos, 2)

        # Рисование при движении
        elif event.type == pygame.MOUSEMOTION and drawing:
            if current_tool in ["PENCIL", "ERASER"]:
                pygame.draw.circle(screen, WHITE if current_tool == "ERASER" else current_color, event.pos, 2)

        # Конец рисования фигуры
        elif event.type == pygame.MOUSEBUTTONUP:
            drawing = False
            if current_tool not in ["PENCIL", "ERASER"]:
                draw_shape(current_tool, start_pos, event.pos, current_color)

        # Горячие клавиши инструментов
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p:
                current_tool = "PENCIL"
            elif event.key == pygame.K_e:
                current_tool = "ERASER"
            elif event.key == pygame.K_r:
                current_tool = "RECT"
            elif event.key == pygame.K_s:
                current_tool = "SQUARE"
            elif event.key == pygame.K_c:
                current_tool = "CIRCLE"
            elif event.key == pygame.K_t:
                current_tool = "TRIANGLE"
            elif event.key == pygame.K_v:
                current_tool = "EQ_TRIANGLE"
            elif event.key == pygame.K_h:
                current_tool = "RHOMBUS"

            # Цвета
            elif event.key == pygame.K_1:
                current_color = BLACK
            elif event.key == pygame.K_2:
                current_color = RED
            elif event.key == pygame.K_3:
                current_color = GREEN
            elif event.key == pygame.K_4:
                current_color = BLUE
            elif event.key == pygame.K_5:
                current_color = WHITE

    pygame.display.flip()
