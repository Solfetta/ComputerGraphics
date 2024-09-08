import math
import pygame

WIDTH = 1500
HEIGHT = 900
FPS = 30
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

pygame.init()
display = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Pifagor_tree')
clock = pygame.time.Clock()


def draw_tree(n, x0, y0, a, fi, alpha):
    x1 = x0
    y1 = y0

    dx = a * math.sin(fi)
    dy = a * math.cos(fi)

    x2 = x0 + dx
    y2 = y0 - dy

    x3 = x0 + dx - dy
    y3 = y0 - dy - dx

    x4 = x0 - dy
    y4 = y0 - dx

    x5 = x0 - dy + a * math.cos(alpha) * math.sin(fi - alpha)
    y5 = y0 - dx - a * math.cos(alpha) * math.cos(fi - alpha)

    pygame.draw.polygon(display, BLACK, [(x1, y1), (x2, y2), (x3, y3), (x4, y4)], width=1)
    pygame.draw.polygon(display, BLACK, [(x4, y4), (x3, y3), (x5, y5)], width=1)
    pygame.display.update()
    if n > 1:
        draw_tree(n - 1, x5, y5, a * math.sin(alpha), fi - alpha + pi / 2, alpha)
        draw_tree(n - 1, x4, y4, a * math.cos(alpha), fi - alpha, alpha)


display.fill(WHITE)
x = 500
y = 800
l = 100
deep = 8
pi = 3.14159265359
fi = pi / 2
alpha = pi / 4  # для получения других видов дерева можно изменять делитель

running = True
while running:
    clock.tick(30)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    draw_tree(deep, x, y, l, fi, alpha)

pygame.quit()
