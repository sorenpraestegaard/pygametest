import pygame
import math

pygame.init()

size = width, height = 320, 240
speed = [2,2]
pos = [150, 100]
black = 0,0,0
time = 0
screen = pygame.display.set_mode(size)

while True:
	time = time + 0.01
	pos[0] = 50 * math.sin(time)

	screen.fill(black)
	pygame.draw.rect(screen, (255, 0, 0), [pos[0], pos[1], 10, 10], 2)
	pygame.display.flip()
