import pygame, sys, socket
from pygame.locals import *
from array import array
from math import *
from soundboard import soundboard
from player import Player

class Healer(Player):
	
	anim_frames=0
	animation=0
	direction=0
	jump=0
	color="original"
	#COLORS SUPPORTED SO FAR:
	# 004c00 : green
	# 0066cc : light blue
	# 460099 : purple
	# 800000 : red
	# e5e600 : yellow
	# 000080 : blue
	# cc5200 : orange
	
	def __init__(self, screen, sound, level, player_pos):
		self.screen=screen
		self.pos=player_pos
		self.stand_sprites = []
		for i in range(1,6):
			string = "images/animations/healer/" + "/healer_idle_" + str(i) + ".png"
			self.stand_sprites.append(pygame.transform.scale2x(pygame.image.load(string)).convert_alpha())
		self.slide_sprite = [pygame.transform.scale2x(pygame.image.load("images/animations/healer/" + "/healer_slide.png")).convert_alpha()]
		self.walk_sprites = []
		for i in range(1,6):
			string = "images/animations/healer/"  + "/healer_walk_" + str(i) + ".png"
			self.walk_sprites.append(pygame.transform.scale2x(pygame.image.load(string)).convert_alpha())
		self.jump_sprites = []
		for i in range(1,13):
			string = "images/animations/healer/"+ "/healer_jump_" + str(i) + ".png"
			self.jump_sprites.append(pygame.transform.scale2x(pygame.image.load(string)).convert_alpha())
		self.fall_sprites = []
		for i in range(1,6):
			string = "images/animations/healer/"+ "/healer_idle_" + str(i) + ".png"
			self.fall_sprites.append(pygame.transform.scale2x(pygame.image.load(string)).convert_alpha())
		
		self.level=level
		self.sounds=sound
	
		
	def update(self, inputs, bullets):
		Player.update(self,inputs, bullets)
		body=Rect((self.pos[0]-32,self.pos[1]-64), (64,64))
		xpos=self.pos[0]
		ypos=self.pos[1]
		if inputs[1]==1:
			self.direction=1
		elif inputs[3]==1:
			self.direction=0
			
		col_index=body.collidelist(self.level)
		if inputs[0] and self.jump==0:
			self.jump=1
		if col_index!=-1:
			plat=self.level[col_index]
			
			if fabs(body.bottom-plat.top)<17:
				self.jump=0
				self.animation=0
				if inputs[1]==1 or inputs[3]==1:
					self.animation=1
			if fabs(body.top-plat.bottom)<10:
				self.animation=3
			
			elif body.bottom>plat.top-3 and body.top<plat.bottom+3:
				if fabs(body.right-plat.left)<8 or fabs(body.left-plat.right)<8:
					self.animation=4
					self.jump=0
		else:
			if ypos < 720:
				self.animation=3
			else:
				self.animation=0
				if inputs[1]==1 or inputs[3]==1:
					self.animation=1
				self.jump=0
			if self.jump > 0:
				self.animation=2
				self.jump+=1
			if self.jump >30:
				self.jump=-1
		self.pos=(xpos, ypos)
		self.anim_frames+=1
		if self .anim_frames==360:
			self .anim_frames=0
		return
		
	
	
	def draw(self):
		if self.direction == 0:
			return (self.getAnimation(), self.getPos())
		else:
			return (pygame.transform.flip(self.getAnimation(), True, False), self.getPos())
		
		
	def getAnimation(self):
		if self.animation==0:
			return self.stand_sprites[(self.anim_frames/10)%len(self.stand_sprites)]
		elif self.animation==1:
			return self.walk_sprites[(self.anim_frames/10)%len(self.walk_sprites)]
		elif self.animation==2:
			return self.jump_sprites[(self.jump/3)%len(self.jump_sprites)]
		elif self.animation==3:
			return self.fall_sprites[(self.anim_frames/10)%len(self.fall_sprites)]
		elif self.animation==4:
			return self.slide_sprite[0]
		