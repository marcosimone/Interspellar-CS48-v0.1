import pygame, sys, socket
from pygame.locals import *
from array import array
from math import *
from soundboard import soundboard
from bullet import Bullet


'''Fire_Ball is the standard spell cast by the Dank_Wizard
   class. It is the average spell that does average damage (75) 
   and goes a normal distance (stub)'''

class Fire_Ball(Bullet):
	anim_frames = 0
	aniimation = 0
	damage = 75
    speed=10
	#Fire_Ball Constructor
	def __init__(self, screen, sound, level, mouse_pos, player_pos):
		sound.fire.play()
		self.screen=screen
		self.frame=0
		self.angle = getAngleBetweenPoints(player_pos[0], mouse_pos[1], mouse_pos[0], player_pos[1])
		self.fireball=[]
		for i in range(1,15):
			name_str = "images/animations/fireball/fireball_" + str(i) + ".png"
			self.fireball.append(pygame.transform.scale2x(pygame.image.load(name_str)).convert_alpha())
			self.fireball[i-1] = pygame.transform.rotate(self.fireball[i-1],self.angle)
		self.pos=(player_pos[0]+16,player_pos[1]+16)
		self.level=level
		self.sounds=sound


		

	def draw(self):
		return (self.getAnimation(), self.getPos())
		
	#The fireball dies out after a few times of running the animation
	#thus, it's range is limited
	def isDead(self):
		dead=(self.pos[0]>1280 or self.pos[0]<0 or self.pos[1]>720 or self.pos[1]<0) 
		if self.frame >= len(self.fireball)*5 -1:
			return True
		for ob in self.level:
			if ob.collidepoint((self.pos[0]-16, self.pos[1]-16)):
				return True
		
		return dead or self.died
	
	#Gets one of two animations for fireball: fired and destruct
	#Animation 1 occurs when the fireball is fired 
	#Animation 2 occurs when self is "dead"
	def getAnimation(self):
		if self.animation==1:
			return self.fired_sprites[(self.anim_frames/10)%len(self.fired_sprites)]
		elif self.animation==2:
			return self.destruct_sprite[self.anim_frames/10)%len(self.destruct_sprite)]



