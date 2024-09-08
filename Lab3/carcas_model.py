from math import *
import numpy as np
import pygame

WIDTH = 1500
HEIGHT = 800


class Object:

    def __init__(self, file):
        self.file = file
        self.points = []
        self.lines = []
        self.get_points()
        self.get_lines()

    def get_points(self):
        n = int(file.readline())
        for i in range(n):
            x = file.readline().split()
            point = []
            for x1 in x:
                point.append(int(x1))
            self.points.append(point)

    def get_lines(self):
        n = int(file.readline())
        for i in range(n):
            x = file.readline().split()
            point = []
            for x1 in x:
                point.append(int(x1) - 1)
            self.lines.append(point)

    def draw_object(self):
        draw_points = []
        for i in object.points:
            draw_points.append(model.prospective(i))
        for i in object.lines:
            pygame.draw.line(display, (0, 0, 0), draw_points[i[0]], draw_points[i[1]], width=3)


class Model:
    def __init__(self, rho=1000, theta=0, phi=0):
        self.factor = atan(1.0) / 45.0
        self.rho = rho
        self.th = theta * self.factor
        self.ph = phi * self.factor

        self.costh = cos(self.th)
        self.sinth = sin(self.th)
        self.cosph = cos(self.ph)
        self.sinph = sin(self.ph)
        self.v11 = -self.sinth
        self.v12 = -self.cosph * self.costh
        self.v13 = -self.sinph * self.costh
        self.v21 = self.costh
        self.v22 = -self.cosph * self.sinth
        self.v23 = -self.sinph * self.sinth
        self.v32 = self.sinph
        self.v33 = -self.cosph
        self.v43 = self.rho

    def prospective(self, koord_w):
        koord_e = [self.v11 * koord_w[0] + self.v21 * koord_w[1],
                   self.v12 * koord_w[0] + self.v22 * koord_w[1] + self.v32 * koord_w[2],
                   self.v13 * koord_w[0] + self.v23 * koord_w[1] + self.v33 * koord_w[2] + self.v43]
        xe = koord_e[0]
        ye = koord_e[1]
        ze = koord_e[2]
        x = self.rho / ze * xe * 1.5 + WIDTH / 2
        y = self.rho / ze * ye * 1.5 + HEIGHT / 2
        return x, y


if (a := int(input('Выберите объект (1 - стул; 2 - куб): '))) == 1:
    file = open("chair.dat", "r")
else:
    file = open("cube.dat", "r")
rho = int(input('Введите расстояние до объекта: '))
phi, theta = 0, 0
object = Object(file)
file.close()
model = Model(rho, phi, theta)

pygame.init()
display = pygame.display.set_mode((1500, 800))
clock = pygame.time.Clock()

running = True
while running:
    clock.tick(30)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    model.__init__(rho, phi, theta)
    display.fill((255, 255, 255))
    object.draw_object()
    pygame.display.update()
    phi += 0.5
    theta += 0.5
    if phi > 360:
        phi = 0
    if theta > 360:
        theta = 0
pygame.quit()
