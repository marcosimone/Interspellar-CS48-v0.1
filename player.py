import pygame, sys, socket
from pygame.locals import *
from array import array
from math import *

class Player:
	health = 1000
	velocity=0
	x=0
	def __init__(self, screen, image, player_pos):
		self.screen=screen
		self.image = image
		self.pos=player_pos
	
	def draw(self):
		self.screen.blit(self.image[(self.x/30)%2], (self.pos[0]-32,self.pos[1]-64))
	
	def isDead(self):
		return (self.health<=0)
	
	def getPos(self):
		return (self.pos[0]-32, self.pos[1]-64)
	
	def update(self, inputs):
		xpos=self.pos[0]
		ypos=self.pos[1]
		
		if ypos < 720:
			self.velocity-=.5
		if ypos==720:
			if inputs[0]:
				self.velocity=15
			else:
				self.velocity=0
		if inputs[1]:
			xpos-=2
		if inputs[3]:
			xpos+=2
		ypos=ypos-self.velocity
		if ypos > 720:
			ypos=720
		if xpos < 0:
			xpos=0
		if xpos > 1280:
			xpos=1280
		self.pos=(xpos, ypos)
		self.x+=1
		if self.x==9000:
			self.x=0
		return