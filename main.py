import pygame, sys
from pygame.locals import *
from array import array

pygame.mixer.pre_init(44100, -16, 2, 512)
pygame.init()
pygame.font.init()
screen = pygame.display.set_mode((1280,720))
fpsClock=pygame.time.Clock()
font=pygame.font.Font('WhiteRabbit.ttf', 24)
icon=pygame.image.load("images/icon.png").convert_alpha()
click = pygame.mixer.Sound("sound/click.wav")
def main():
	
	pygame.mixer.music.load("sound/Lines_of_Code.wav")
	pygame.display.set_caption('Interspellar')
	pygame.display.set_icon(icon)

	mainMenu()



	
def mainMenu():
	logo=pygame.image.load("images/logo.png").convert_alpha()
	stars=pygame.image.load("images/stars.png").convert_alpha()
	stars2=stars
	hills=pygame.image.load("images/hills.png").convert_alpha()
	
	
	button=pygame.image.load("images/buttons/button.png").convert_alpha()
	button_hover=pygame.image.load("images/buttons/button_hover.png").convert_alpha()
	
	buttons_idle=[pygame.image.load("images/buttons/play.png").convert_alpha(),pygame.image.load("images/buttons/options.png").convert_alpha(),pygame.image.load("images/buttons/credits.png").convert_alpha()]
	buttons_hover=[pygame.image.load("images/buttons/play_hover.png").convert_alpha(),pygame.image.load("images/buttons/options_hover.png").convert_alpha(),pygame.image.load("images/buttons/credits_hover.png").convert_alpha()]
	buttons=[buttons_idle[0],buttons_idle[1],buttons_idle[2]]
	
	y=0
	screen.blit(stars, (0,y))
	screen.blit(stars, (0,y-720))
	screen.blit(hills, (0,720-hills.get_height()))
	screen.blit(logo,(254,131))
	for index,butt in enumerate(buttons):
		screen.blit(butt, (500, 300+(100*index)))

	pygame.mixer.music.play(-1)
	while 1:
		for index,butt in enumerate(buttons):
			if Rect(500,300+(100*index),butt.get_width(), butt.get_height()).collidepoint(pygame.mouse.get_pos()):
				buttons[index]=buttons_hover[index]
			else:
				buttons[index]=buttons_idle[index]
		screen.blit(stars, (0,y/2))
		screen.blit(stars, (0,y/2-720))
		screen.blit(hills, (0,720-hills.get_height()))
		screen.blit(logo,(254,131))
		for index,butt in enumerate(buttons):
			screen.blit(butt, (500, 300+(100*index)))
		y+=1
		if y==1440:
			y=0
		for event in pygame.event.get():

			if event.type==QUIT:
				pygame.quit()
				sys.exit()
			if event.type==MOUSEBUTTONUP:
				for index,butt in enumerate(buttons):
					if Rect(500,300+(100*index),butt.get_width(), butt.get_height()).collidepoint(pygame.mouse.get_pos()):
						click.play()
						menu_choices[index]()
		
		
		
		pygame.display.update()
		pygame.display.set_caption("fps: " + str(fpsClock.get_fps()))
		fpsClock.tick(60)


def play():
	print "you clicked play"
def options():
	print "you clicked options"
def credits():
	print "you clicked credits"

menu_choices=[play,options,credits]





if __name__=="__main__":
   main()

