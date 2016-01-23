import pygame, sys, socket
from pygame.locals import *
from array import array

pygame.mixer.pre_init(44100, -16, 2, 512) 
pygame.init() 
pygame.font.init()
screen = pygame.display.set_mode((1280,720)) 
fpsClock=pygame.time.Clock() 
font=pygame.font.Font('WhiteRabbit.ttf', 24)
icon=pygame.image.load("images/icon.png").convert_alpha()
y=0
#sound
click = pygame.mixer.Sound("sound/click.wav")

#background stuff
logo=pygame.image.load("images/logo.png").convert_alpha()
stars=pygame.image.load("images/stars.png").convert_alpha()
stars2=stars
hills=pygame.image.load("images/hills.png").convert_alpha()

#buttons
back_hover=pygame.image.load("images/buttons/back_hover.png").convert_alpha()
back_idle=pygame.image.load("images/buttons/back.png").convert_alpha()

#networking
sock=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

def main(): 
	
	pygame.mixer.music.load("sound/Lines_of_Code.wav")
	pygame.display.set_icon(icon)

	mainMenu() 



	
def mainMenu():
	
	buttons_idle=[pygame.image.load("images/buttons/play.png").convert_alpha(),pygame.image.load("images/buttons/options.png").convert_alpha(),pygame.image.load("images/buttons/credits.png").convert_alpha()]
	buttons_hover=[pygame.image.load("images/buttons/play_hover.png").convert_alpha(),pygame.image.load("images/buttons/options_hover.png").convert_alpha(),pygame.image.load("images/buttons/credits_hover.png").convert_alpha()]
	buttons=[buttons_idle[0],buttons_idle[1],buttons_idle[2]] 
	
	global y
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
			sock.sendto(str(event),("127.0.0.1", 4637))
			if event.type==QUIT: 
				pygame.quit()
				sys.exit()
				
			if event.type==MOUSEBUTTONUP and event.button==1:
				for index,butt in enumerate(buttons):
					if Rect(500,300+(100*index),butt.get_width(), butt.get_height()).collidepoint(event.pos):
						click.play()
						menu_choices[index]() 
						
			if pygame.key.get_pressed()==(0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0):
				pygame.mouse.set_cursor((24,24),(0,10),*cursor)
							
		pygame.display.update()
		pygame.display.set_caption("Interspellar fps: " + str(fpsClock.get_fps()))
		fpsClock.tick(60)

def play():
	print "you clicked play"
def options():
	global y
	back=back_idle
	while 1:
		screen.blit(stars, (0,y/2))
		screen.blit(stars, (0,y/2-720))
		screen.blit(hills, (0,720-hills.get_height()))
		screen.blit(back, (100, 575))
		y+=1
		if y==1440:
			y=0
			
		if Rect(100,575,back.get_width(), back.get_height()).collidepoint(pygame.mouse.get_pos()):
			back=back_hover
		else:
			back=back_idle
		
		for event in pygame.event.get():
			if event.type==QUIT:
				pygame.quit()
				sys.exit()
			if event.type==MOUSEBUTTONUP and event.button==1:
				if Rect(100,575,back.get_width(), back.get_height()).collidepoint(event.pos):
					click.play()
					return
		pygame.display.update() 
		pygame.display.set_caption("Interspellar fps: " + str(fpsClock.get_fps()))
		fpsClock.tick(60) 
def credits():
	walker=[pygame.transform.scale2x(pygame.image.load("images/animations/shadowmage walk_1.png").convert_alpha()),pygame.transform.scale2x(pygame.image.load("images/animations/shadowmage walk_2.png").convert_alpha()),pygame.transform.scale2x(pygame.image.load("images/animations/shadowmage walk_3.png").convert_alpha()),pygame.transform.scale2x(pygame.image.load("images/animations/shadowmage walk_4.png").convert_alpha())]
	global y
	x=0
	back=back_idle
	while 1:
		screen.blit(stars, (0,y/2))
		screen.blit(stars, (0,y/2-720))
		screen.blit(hills, (0,720-hills.get_height()))
		screen.blit(back, (100, 575))
		x+=1
		if x>=1280+64:
			screen.blit(pygame.transform.flip(walker[(x/9)%4],True,False), ((x-1280-64-64),650))
			if x==2*(1280+64):
				x=0
		else:
			screen.blit(walker[(x/9)%4], (1280-x,650))
		y+=1
		if y==1440:
			y=0
			
		if Rect(100,575,back.get_width(), back.get_height()).collidepoint(pygame.mouse.get_pos()):
			back=back_hover
		else:
			back=back_idle
		
		for event in pygame.event.get():
			if event.type==QUIT:
				pygame.quit()
				sys.exit()
			if event.type==MOUSEBUTTONUP and event.button==1:
				if Rect(100,575,back.get_width(), back.get_height()).collidepoint(event.pos):
					click.play()
					return
		pygame.display.update() 
		pygame.display.set_caption("Interspellar fps: " + str(fpsClock.get_fps()))
		fpsClock.tick(60) 

menu_choices=[play,options,credits]


lol=("         xxxx           ","       xx....xx         ","      xx......xx        ","       xx....xx         ","       xx....xx         ","       xx....xx         ","       xx....xx         ","       xx....xx         ","       xx....xx         ","       xx....xx         ","       xx....xx         ","      xxx....xxx        ","     xxx......xxx       ","    xx..........xx      ","   xx............xx     ","  xx..............xx    ","   xx.....xx.....xx     ","     xxxxx  xxxxx       ","                        ","                        ","                        ","                        ","                        ","                        ")
cursor = pygame.cursors.compile(lol,'o', white='.', xor='x')

  

if __name__=="__main__":
   main()

