import pygame, sys
from pygame.locals import *
from array import array

pygame.init()
pygame.font.init()
screen = pygame.display.set_mode((1280,720))
fpsClock=pygame.time.Clock()
font=pygame.font.Font('WhiteRabbit.ttf', 24)
icon=pygame.image.load("images/icon.png").convert_alpha()

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
	button=pygame.image.load("images/button.png").convert_alpha()
	button_hover=pygame.image.load("images/button_hover.png").convert_alpha()
	butt=button
	buttRect=Rect(500,300,butt.get_width(), butt.get_height())
	
	y=0
	screen.blit(stars, (0,y))
	screen.blit(stars, (0,y-720))
	screen.blit(hills, (0,720-hills.get_height()))
	screen.blit(logo,(254,131))
	screen.blit(butt, (500, 300))
	pygame.mixer.music.play(-1)
	while 1:
		if buttRect.collidepoint(pygame.mouse.get_pos()):
			butt=button_hover
		else:
			butt=button
		screen.blit(stars, (0,y/2))
		screen.blit(stars, (0,y/2-720))
		screen.blit(hills, (0,720-hills.get_height()))
		screen.blit(logo,(254,131))
		screen.blit(butt, (500, 300))
		y+=1
		if y==1440:
			y=0
		for event in pygame.event.get():
			if event.type==QUIT:
				pygame.quit()
				sys.exit()
			if event.type==MOUSEBUTTONUP:
				if buttRect.collidepoint(pygame.mouse.get_pos()):
					print "button clicked"
		
		
		
		pygame.display.update()
		pygame.display.set_caption("fps: " + str(fpsClock.get_fps()))
		fpsClock.tick(60)








if __name__=="__main__":
   main()

