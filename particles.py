from math import sin
from random import randint
import pygame

class Particle():

    def __init__(self, posx, posy):
        col = randint(0,255)
        self.col = (col, col, col)
        self.startpos = [posx, posy]
        self.pos = [posx, posy]
        self.dy = float(randint(1,5))/100
        self.dx = randint(3,5)

    def move(self, t):
        dist = abs(self.startpos[0] - self.pos[0])
        if dist < 100:
            self.pos[0] += self.dx * dist/100 * sin(t)
            self.pos[1] += self.dy
        else:
            self.pos[0] = self.startpos[0]
            self.pos[1] = self.startpos[1]

    def draw_particle(self, display):
        pygame.draw.circle(display, self.col, (int(self.pos[0]), int(self.pos[1])), 2)
