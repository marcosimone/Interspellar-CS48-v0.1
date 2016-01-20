import pygame, sys
from pygame.locals import *

pygame.init()
pygame.font.init()
fpsClock=pygame.time.Clock()

screen = pygame.display.set_mode((1280,720))
pygame.display.set_caption('Interspellar')
font=pygame.font.Font('fipps.ttf', 24)
logo=pygame.image.load("images/logo.png").convert_alpha()
icon=pygame.image.load("images/icon.png").convert_alpha()
stars=pygame.image.load("images/stars.png").convert_alpha()
stars2=stars
hills=pygame.image.load("images/hills.png").convert_alpha()
pygame.display.set_icon(icon)
y=0
screen.blit(stars, (0,y))
screen.blit(stars, (0,y-720))
screen.blit(hills, (0,720-hills.get_height()))
screen.blit(logo,(254,131))


while 1:
	screen.blit(stars, (0,y))
	screen.blit(stars, (0,y-720))
	screen.blit(hills, (0,720-hills.get_height()))
	screen.blit(logo,(254,131))
	y+=.5
	if y==720:
		y=0
	for event in pygame.event.get():
		if event.type==QUIT:
			pygame.quit()
			sys.exit()
	
	
	
	pygame.display.update()
	fpsClock.tick(60)
