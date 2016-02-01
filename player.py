import pygame, sys, socket
from pygame.locals import *
from array import array
from math import *
from soundboard import soundboard

class Player:
	health = 1000
	velocity=0
	xvelocity=0
	anim_frame=0
	def __init__(self, screen, sound, level, player_pos):
		self.screen=screen
		self.image = [pygame.transform.scale2x(pygame.image.load("images/animations/floating_blood_1.png").convert_alpha()),pygame.transform.scale2x(pygame.image.load("images/animations/floating_blood_2.png").convert_alpha())]
		self.pos=player_pos
		self.level=level
		self.sounds=sound
	
	def draw(self):
		return (self.image[(self.anim_frame/30)%2], self.getPos())
	
	def isDead(self):
		return (self.health<=0)
	
	def getPos(self):
		return (self.pos[0]-32, self.pos[1]-64)
	
	def setPos(self, pos):
		self.pos=(pos[0]+32,pos[1]+64)
	
	def update(self, inputs, bullets):
		body=Rect((self.pos[0]-32,self.pos[1]-64), (64,64))
		xpos=self.pos[0]
		ypos=self.pos[1]
		
		for bullet in bullets:
			if body.collidepoint(bullet.getPos()) and (bullet.player!="me"):
				bullet.selfDestruct()
				self.health-=100
				print self.health
				if isDead():
					sys.exit()
		
		col_index=body.collidelist(self.level)
		if self.velocity < -15:
			self.velocity =-15
		if col_index!=-1:
			plat=self.level[col_index]
			
			if fabs(body.bottom-plat.top)<17:
				self.velocity=0
				if inputs[0]:
					ypos=plat.top-10
					self.velocity=15
			if fabs(body.top-plat.bottom)<10:
				self.velocity=-1.0
				
			
			elif body.bottom>plat.top-3 and body.top<plat.bottom+3:
				if fabs(body.right-plat.left)<8:
					if self.velocity > 5:
						self.velocity-=1.5
					else:
						self.velocity-=0.1
					if self.velocity < -5:
						self.velocity = -5
					xpos=plat.left-32
					if inputs[0]:
						self.velocity = 10
						self.xvelocity = -8
						
				elif fabs(body.left-plat.right)<8:
					if self.velocity > 5:
						self.velocity-=1.5
					else:
						self.velocity-=0.1
					if self.velocity < -5:
						self.velocity = -5
					xpos=plat.right+32
					if inputs[0]:
						self.velocity = 10
						self.xvelocity = 8
						
		else:
			if ypos <=32:
				self.velocity=-1
			if ypos < 720:
				self.velocity-=.5
			else:
				if inputs[0]:
					self.velocity=15
				else:
					self.velocity=0
		ypos=ypos-self.velocity
		xpos=xpos+self.xvelocity
		if self.xvelocity > 0:
			self.xvelocity-=0.4
		if self.xvelocity < 0:
			self.xvelocity+=0.4
		if fabs(self.xvelocity) < 0.5:
			self.xvelocity = 0
		if inputs[1]:
			xpos-=4
		if inputs[3]:
			xpos+=4
		if xpos < 32:
			xpos=32
		if xpos > 1248:
			xpos=1248
		if ypos > 720:
			ypos=720
		self.pos=(xpos, ypos)
		self .anim_frame+=1
		if self .anim_frame==9000:
			self .anim_frame=0
		return
		