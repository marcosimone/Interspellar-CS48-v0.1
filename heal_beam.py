import pygame, sys, socket
from pygame.locals import *
from array import array
from math import *
from soundboard import soundboard
from bullet import *

class Heal(Bullet):

    speed=8
    died=False
    player="me"
    
    id=0 #will determine speed and damage
    def __init__(self, screen, sound, level, id, mouse_pos, player_pos):
        self.hearts=[]
        sound.fire.play()
        self.id=id
        self.screen=screen
        self.frame=0
        self.damage=-100
        self.angle = getAngleBetweenPoints(player_pos[0], mouse_pos[1], mouse_pos[0], player_pos[1])
        for i in range(1,11):
            name_str = "images/animations/heal_beam/heal_" + str(i) + ".png"
            self.hearts.append(pygame.transform.scale2x(pygame.image.load(name_str)).convert_alpha())
            if mouse_pos[0] < player_pos[0]:
                self.hearts[i-1] = pygame.transform.flip(self.hearts[i-1], False, True)
            self.hearts[i-1] = pygame.transform.rotate(self.hearts[i-1],self.angle)
        self.pos=(player_pos[0],player_pos[1])
        self.level=level
        self.sounds=sound
        self.hbox = Rect((player_pos[0],player_pos[1]),(64 , 32))
        
    def hitbox(self):
        self.hbox=Rect((self.pos[0], self.pos[1]), (64,32))
    def getType(self):
        return "heal"
    
    def draw(self):
        self.hitbox()
        return (self.hearts[((int(self.frame)/5)%len(self.hearts))],(self.pos[0], self.pos[1]))

    def hitbox(self):
        self.hbox=Rect((self.pos[0], self.pos[1]+16), (32,32))
        
    def isDead(self):
        dead=(self.pos[0]>1280 or self.pos[0]<0 or self.pos[1]>720 or self.pos[1]<0) 
        if self.frame >= len(self.hearts)*5 -1:
            return True

        if self.hbox.collidelist(self.level) == -1:
            return False
        else:
            return True
        return dead or self.died
      
    def selfDestruct(self):
        self.died=True
  
   
    def toString(self):
        return "%d,%d,%d" % (self.pos[0],self.pos[1],self.angle)
        
    def getPos(self):
        return self.pos
    
    