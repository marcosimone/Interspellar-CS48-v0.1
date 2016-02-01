import pygame, sys, socket
from pygame.locals import *
from array import array
from math import *
from soundboard import soundboard
def angle_trunc(a):
	while a < 0.0:
		a += pi * 2
	return a*(360/(2*pi))

def getAngleBetweenPoints(x_orig, y_orig, x_landmark, y_landmark):
	deltaY = y_landmark - y_orig
	deltaX = x_landmark - x_orig
	return angle_trunc(atan2(deltaY, deltaX))

class Bullet:
	speed=10
	died=False
	player="me"
	def __init__(self, screen, sound, level, mouse_pos, player_pos):
		sound.fire.play()
		self.screen=screen
		self.angle = getAngleBetweenPoints(player_pos[0], mouse_pos[1], mouse_pos[0], player_pos[1])
		image=pygame.image.load("images/animations/bullet.png").convert_alpha()
		self.image = pygame.transform.rotate(image,-45)
		self.image = pygame.transform.rotate(image,self.angle-45)
		self.pos=(player_pos[0]+16,player_pos[1]+16)
		self.level=level
		self.sounds=sound

	
	def draw(self):
		return (self.image,(self.pos[0]-16, self.pos[1]-16))
	
	def isDead(self):
		dead=(self.pos[0]>1280 or self.pos[0]<0 or self.pos[1]>720 or self.pos[1]<0) 
		for ob in self.level:
			if ob.collidepoint((self.pos[0]-16, self.pos[1]-16)):
				return True
		
		return dead or self.died
		
	def selfDestruct(self):
		self.died=True
	
	def update(self):
		rad=radians(self.angle)
		self.pos=(self.pos[0]+(self.speed*cos(rad)), self.pos[1]-(self.speed*sin(rad)))

	def toString(self):
		return "%d,%d,%d" % (self.pos[0],self.pos[1],self.angle)
		
	def getPos(self):
		return self.pos
		
class enemyBullet(Bullet):
	speed=10
	player="enemy"
	def __init__(self, screen, sound, level, bulletString):
		params=bulletString.split(',')
		self.pos=(float(params[0]),float(params[1]))
		sound.fire.play()
		self.screen=screen
		self.angle = float(params[2])
		image=pygame.image.load("images/animations/bullet.png").convert_alpha()
		self.image = pygame.transform.rotate(image,-45)
		self.image = pygame.transform.rotate(image,self.angle-45)
		self.level=level
		self.sounds=sound
	
	