import pygame, sys, socket
from pygame.locals import *
from array import array

pygame.mixer.pre_init(44100, -16, 2, 512) #pre_init will change what settings the sound will init with, we're initting with a lower buffer size(512) to reduce sound response lag
pygame.init() #init the pygame module
pygame.font.init()
screen = pygame.display.set_mode((1280,720)) #init our screen
fpsClock=pygame.time.Clock() #start clock (used to regulate fps)
font=pygame.font.Font('WhiteRabbit.ttf', 24)
icon=pygame.image.load("images/icon.png").convert_alpha() #loading icon 
click = pygame.mixer.Sound("sound/click.wav") #loading click sound to use later

sock=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

def main(): #NOTE: python doesnt actually call main to start, at the bottom I am calling it.  if you want more detail why then just ask
	
	pygame.mixer.music.load("sound/Lines_of_Code.wav") #loading menu music
	pygame.display.set_icon(icon) #setting the icon

	mainMenu() #starting the mainMenu sequence



	
def mainMenu():
	#loading all the images for menu
	logo=pygame.image.load("images/logo.png").convert_alpha()
	stars=pygame.image.load("images/stars.png").convert_alpha()
	stars2=stars
	hills=pygame.image.load("images/hills.png").convert_alpha()
	
	#creating an array of buttons to organize them, there are two versions of each button. one for idle and one when the user is hovering over it
	buttons_idle=[pygame.image.load("images/buttons/play.png").convert_alpha(),pygame.image.load("images/buttons/options.png").convert_alpha(),pygame.image.load("images/buttons/credits.png").convert_alpha()]
	buttons_hover=[pygame.image.load("images/buttons/play_hover.png").convert_alpha(),pygame.image.load("images/buttons/options_hover.png").convert_alpha(),pygame.image.load("images/buttons/credits_hover.png").convert_alpha()]
	buttons=[buttons_idle[0],buttons_idle[1],buttons_idle[2]] #initialize the buttons to the idle versions
	
	y=0 #used to maintain the scrolling stars.  two copies scroll continuously to create the effect
	screen.blit(stars, (0,y))
	screen.blit(stars, (0,y-720))
	screen.blit(hills, (0,720-hills.get_height()))
	screen.blit(logo,(254,131))
	
	#draw the buttons by looping through the button array
	for index,butt in enumerate(buttons):
		screen.blit(butt, (500, 300+(100*index)))

	pygame.mixer.music.play(-1) #start the music
	while 1: #game loop
	
		#check if mouse is hovering over a button, if so, then swap out the idle button for the hover button
		for index,butt in enumerate(buttons):
			if Rect(500,300+(100*index),butt.get_width(), butt.get_height()).collidepoint(pygame.mouse.get_pos()):
				buttons[index]=buttons_hover[index]
			else:
				buttons[index]=buttons_idle[index]
		
		#draw everything		
		screen.blit(stars, (0,y/2))
		screen.blit(stars, (0,y/2-720))
		screen.blit(hills, (0,720-hills.get_height()))
		screen.blit(logo,(254,131))
		for index,butt in enumerate(buttons):
			screen.blit(butt, (500, 300+(100*index)))
		y+=1
		if y==1440: #once the stars reach the bottom of the screen, they will be moved to the top to maintain the scrolling
			y=0
			
		#pygame maintains a queue of events that happen, here we loop through them 
		for event in pygame.event.get():
			print event
			sock.sendto(str(event),("127.0.0.1", 4637))
			if event.type==QUIT: #checks if the close button on the window is clicked, if so, then uninitialize pygame before quitting
				pygame.quit()
				sys.exit()
				
			#check for click release and that the button was left click (button id=1 for left click)
			if event.type==MOUSEBUTTONUP and event.button==1:
				for index,butt in enumerate(buttons):
					if Rect(500,300+(100*index),butt.get_width(), butt.get_height()).collidepoint(event.pos):
						click.play() #if a button was clicked, then we will play our clicking sound
						menu_choices[index]() #array of functions (weird, i know) and we call a different function depending on what button was clicked
			
		pygame.display.update() #update the graphics, this is where all of the things drawn above will be actually displayed on the screen
		pygame.display.set_caption("Interspellar fps: " + str(fpsClock.get_fps())) #update the fps counter in the title
		fpsClock.tick(60) #regulate fps to 60 fps

#functions to be called when the buttons are clicked
def play():
	print "you clicked play"
def options():
	print "you clicked options"
def credits():
	print "you clicked credits"

menu_choices=[play,options,credits] #our array of functions


lol=("                        ","                        ","                        ","                        ","         xxxx           ","       xx....xx         ","      xx......xx        ","       xx....xx         ","       xx....xx         ","       xx....xx         ","       xx....xx         ","      xxx....xxx        ","     xxx......xxx       ","    xx..........xx      ","   xx............xx     ","  xx..............xx    ","   xx.....xx.....xx     ","     xxxxx  xxxxx       ","                        ","                        ","                        ","                        ","                        ","                        ")
cursor = pygame.cursors.compile(lol,'o', white='.', xor='x')
pygame.mouse.set_cursor((24,24),(4,9),*cursor)
  
#this is what calls our main function to kick off the whole thing.  the reason we do it like this is because in python you cant use a function unless it is defined above.  so this means that all the functions will be defined then main will be called here.
if __name__=="__main__":
   main()

