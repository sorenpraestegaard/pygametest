from math import sin
from random import randint
import pygame

class Particle():

    def __init__(self, posx, posy):
        col = randint(0,255)
        self.col = (col, col, col)
        self.startpos = [posx, posy]
        self.pos = [posx, posy]
        self.dy = float(randint(200,700))/10000
        self.dx = randint(3,7)
        self.start_time = pygame.time.get_ticks() + randint(0,100)
        self.w = randint(1,100)/100

    def move(self, t):
        dist = abs(self.startpos[1] - self.pos[1])
        if dist < 100:
            self.pos[0] = self.startpos[0] + self.dx * (float(dist)/100) * sin((t- self.start_time)/self.w)
            self.pos[1] += self.dy
        else:
            self.pos[0] = self.startpos[0]
            self.pos[1] = self.startpos[1]
            self.start_time = pygame.time.get_ticks()

    def draw_particle(self, display):
        pygame.draw.circle(display, self.col, (int(self.pos[0]), int(self.pos[1])), 2)
