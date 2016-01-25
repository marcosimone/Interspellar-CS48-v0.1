import pygame, sys, socket
from pygame.locals import *
from array import array
from bullet import Bullet
from player import Player
from soundboard import soundboard
import pickle

pygame.mixer.pre_init(44100, -16, 2, 512) 
pygame.init() 
pygame.font.init()
screen = pygame.display.set_mode((1280,720)) 
fpsClock=pygame.time.Clock() 
font=pygame.font.Font('WhiteRabbit.ttf', 24)
icon=pygame.image.load("images/icon.png").convert_alpha()
sounds = soundboard()
y=0


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
			if event.type==QUIT: 
				pygame.quit()
				sys.exit()
				
			if event.type==MOUSEBUTTONUP and event.button==1:
				for index,butt in enumerate(buttons):
					if Rect(500,300+(100*index),butt.get_width(), butt.get_height()).collidepoint(event.pos):
						sounds.click.play()
						menu_choices[index]() 
						
			if pygame.key.get_pressed()==(0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0):
				pygame.mouse.set_cursor((24,24),(0,10),*cursor)
							
		pygame.display.update()
		pygame.display.set_caption("Interspellar fps: " + str(fpsClock.get_fps()))
		fpsClock.tick(60)

def play():
	print "you clicked play"
def credits():
	level=[Rect((100,575),(300,70)), Rect((300,175),(300,70)), Rect((200,375),(100,20)), Rect((800,200),(100,500)), Rect((1100,200),(100,500))]
	player=Player(screen, sounds, level, (640, 650))
	other_players=[]
	bullets=[]
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
					sounds.click.play()
					return
			if event.type==MOUSEBUTTONDOWN and event.button==3:
				bullets.append(Bullet(screen, sounds, level, event.pos, player.getPos()))
		
		for bullet in enumerate(bullets):
			if bullet[1].isDead():
				sounds.explode.play()
				del bullets[bullet[0]]
			else:
				bullet[1].update()
				bullet[1].draw()
		input = [pygame.key.get_pressed()[119]==1,pygame.key.get_pressed()[97]==1,pygame.key.get_pressed()[115]==1,pygame.key.get_pressed()[100]==1]
		player.update(input)
		sock.sendto(pickle.dumps(input),("192.168.1.10", 4637))
		
		for other in other_players:
			data, addr = sock.recvfrom(1024)
			data=pickle.loads(data)
			#print data[0]
			if data[0] != '192.168.1.110':
				other.update(data[1])
				other.draw()
		player.draw()
		pygame.display.update() 
		pygame.display.set_caption("Interspellar fps: " + str(fpsClock.get_fps()))
		fpsClock.tick(60) 
def options():
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
					sounds.click.play()
					return
		pygame.display.update() 
		pygame.display.set_caption("Interspellar fps: " + str(fpsClock.get_fps()))
		fpsClock.tick(60) 

menu_choices=[play,options,credits]


lol=("         xxxx           ","       xx....xx         ","      xx......xx        ","       xx....xx         ","       xx....xx         ","       xx....xx         ","       xx....xx         ","       xx....xx         ","       xx....xx         ","       xx....xx         ","       xx....xx         ","      xxx....xxx        ","     xxx......xxx       ","    xx..........xx      ","   xx............xx     ","  xx..............xx    ","   xx.....xx.....xx     ","     xxxxx  xxxxx       ","                        ","                        ","                        ","                        ","                        ","                        ")
cursor = pygame.cursors.compile(lol,'o', white='.', xor='x')

  

if __name__=="__main__":
   main()

