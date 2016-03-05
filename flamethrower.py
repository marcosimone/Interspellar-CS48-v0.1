import pygame, sys, socket
from pygame.locals import *
from array import array
from math import *
from soundboard import soundboard
from bullet import *


"""Flamethrower is a cone of fire that has a set
   radius and cooldown time"""

class Flamethrower(Bullet):
	anim_frames = 0
	aniimation = 0
	damage=60
	
	#Flamethrower Constructor
	def __init__(self, screen, sound, level, mouse_pos, player_pos):
		self.flamethrower=[]
		sound.fire.play()
		self.screen=screen
		self.frame=0
		self.angle = getAngleBetweenPoints(player_pos[0], mouse_pos[1], mouse_pos[0], player_pos[1])
		self.Flamethrower=[]
		for i in range(1,13):
			name_str = "images/animations/Flamethrower/" + str(i) + ".png"
			self.flamethrower.append(pygame.transform.scale2x(pygame.image.load(name_str)).convert_alpha())
			self.flamethrower[i-1] = pygame.transform.rotate(self.flamethrower[i-1],self.angle)
		self.pos=(player_pos[0]-32,player_pos[1]-32)
		self.level=level
		self.sounds=sound
	
	def isDead(self):
		dead=(self.pos[0]>1280 or self.pos[0]<0 or self.pos[1]>720 or self.pos[1]<0) 
		if self.frame >= len(self.flamethrower)*5 -1:
			return True
		for ob in self.level:
			if ob.collidepoint((self.pos[0]-16, self.pos[1]-16)):
				return True
		return dead or self.died

	def draw(self):
		self.hitbox()
		return (self.flamethrower[((self.frame/5)%14)],(self.pos[0], self.pos[1]))

	def getAnimation(self):
		if self.animation==1:
			return self.fired_sprites[(self.anim_frames/10)%len(seld.fired_sprites)]
		elif self.animation==2:
			return self.destruct_sprite[(self.anim_frames/10)%len(self.destruct_sprite)]

	def update(self):
		self.frame+=1
		rad=radians(self.angle)
		self.pos=((self.pos[0]+self.speed*cos(rad)), self.pos[1]-(self.speed*sin(rad)))
		self.hbox=((self.pos[0] + self.speed*cos(rad)), self.pos[1]-(self.speed*sin(rad)))
	
	def toString(self):
		return "%d,%d,%d" % (self.pos[0],self.pos[1],self.angle)

	def getPos(self):
		return self.pos