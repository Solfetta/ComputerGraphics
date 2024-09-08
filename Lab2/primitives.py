from random import randint
import pygame

PIXEL = 3
WIDTH = PIXEL * 240
HEIGHT = PIXEL * 160
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
COLOR = WHITE


class Pixel:
    def __init__(self, x, y, dot_color):
        self.x = int(x)
        self.y = int(y)
        self.dot_color = dot_color
        self.rect = pygame.Rect(self.x * PIXEL, self.y * PIXEL, PIXEL, PIXEL)

    def setColor(self, color):
        self.dot_color = color


class Pixels:
    def __init__(self):
        self.inner = []
        for i in range(int(WIDTH)):
            for j in range(int(HEIGHT)):
                self.inner.append(Pixel(j, i, COLOR))

    def get_pixel(self, x, y):
        for dot in self.inner:
            if dot.x == x and dot.y == y:
                return dot
        return None

    def put_pixel(self, x, y, color):
        self.get_pixel(x, y).setColor(color)

    def draw_line(self, x1, y1, x2, y2, color):
        delta_x = abs(x2 - x1)
        delta_y = abs(y2 - y1)
        sign_x = 1 if x1 < x2 else -1
        sign_y = 1 if y1 < y2 else -1
        error = delta_x - delta_y
        self.put_pixel(x2, y2, color)
        while x1 != x2 or y1 != y2:
            self.put_pixel(x1, y1, color)
            error_2 = error * 2

            if error_2 > -delta_y:
                error -= delta_y
                x1 += sign_x

            if error_2 < delta_x:
                error += delta_x
                y1 += sign_y

    def draw_circle(self, x, y, r, color):
        p, q = 0, r
        d = 1 - 2 * r
        while p <= q:
            self.put_pixel(x + p, y + q, color)
            self.put_pixel(x - p, y + q, color)
            self.put_pixel(x + p, y - q, color)
            self.put_pixel(x - p, y - q, color)
            self.put_pixel(x + q, y + p, color)
            self.put_pixel(x - q, y + p, color)
            self.put_pixel(x + q, y - p, color)
            self.put_pixel(x - q, y - p, color)
            if d <= 0:
                d = d + 4 * p + 6
            else:
                d = d + 4 * (p - q) + 10
                q -= 1
            p += 1

    def draw_picture(self):
        for dot in self.inner:
            pygame.draw.rect(display, dot.dot_color, dot.rect)


pygame.init()
display = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Двумерные примитивы')
clock = pygame.time.Clock()
pixels = Pixels()
dots = []
circle = False

running = True
while running:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                circle = not circle
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            x, y = mouse_pos[0] // PIXEL, mouse_pos[1] // PIXEL
            dots.append((x, y))
            pixel = pixels.get_pixel(x, y)
            if pixel and not circle:
                pixels.put_pixel(x, y, BLACK)
        elif event.type == pygame.MOUSEBUTTONUP:
            if circle:
                pixels.draw_circle(x, y, randint(1, 20), BLACK)
                dots.clear()
            else:
                mouse_pos = pygame.mouse.get_pos()
                x, y = mouse_pos[0] // PIXEL, mouse_pos[1] // PIXEL
                dots.append((x, y))
                pixel = pixels.get_pixel(x, y)
                if pixel and len(dots) == 2:
                    pixels.draw_line(dots[0][0], dots[0][1], dots[1][0], dots[1][1], BLACK)
                    dots.clear()

    display.fill(WHITE)
    pixels.draw_picture()
    pygame.display.update()

pygame.quit()
