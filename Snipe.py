import pygame, sys, socket
from pygame.locals import *
from array import array
from math import *
from soundboard import soundboard
from bullet import *


"""Snipe is a fast moving shot that traverses 
   the entire map and does significant damage"""

class Snipe(Bullet):
	anim_frames = 0
	aniimation = 0
	speed=25
	damage=150
	
	
	#Snipe Constructor
	def __init__(self, screen, sound, level, mouse_pos, player_pos):
		self.snipe=[]
		sound.fire.play()
		self.screen=screen
		self.frame=0
		self.angle = getAngleBetweenPoints(player_pos[0], mouse_pos[1], mouse_pos[0], player_pos[1])
		for i in range(1,15):
			name_str = "images/animations/fireball/fireball_" + str(i) + ".png"
			self.snipe.append(pygame.transform.scale2x(pygame.image.load(name_str)).convert_alpha())
			self.snipe[i-1] = pygame.transform.rotate(self.snipe[i-1],self.angle)
		self.pos=(player_pos[0]-16,player_pos[1]-16)
		self.level=level
		self.sounds=sound
	
	def isDead(self):
		dead=(self.pos[0]>1280 or self.pos[0]<0 or self.pos[1]>720 or self.pos[1]<0) 
		for ob in self.level:
			if ob.collidepoint((self.pos[0]+16, self.pos[1]+16)):
				return True
		return dead or self.died

	def draw(self):
		self.hitbox()
		return (self.snipe[((self.frame/5)%14)],(self.pos[0], self.pos[1]))

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