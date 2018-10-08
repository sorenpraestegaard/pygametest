import pygame
import math
from particles import Particle

pygame.init()

size = width, height = 640, 480
speed = [2,2]
pos = [150, 100]
black = 0,0,0
time = 0
screen = pygame.display.set_mode(size)
running = True
particles = []

for i in range(100):
	particles.append(Particle(100,50))

while running:
	time = pygame.time.get_ticks()
	for event in pygame.event.get():
			if event.type == pygame.QUIT:
				running = False

	for p in particles:
		p.move(time)

	screen.fill(black)
	for p in particles:
		p.draw_particle(screen)
	pygame.display.flip()

pygame.display.quit()
pygame.quit()
