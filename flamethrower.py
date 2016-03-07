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
    damage=150
    speed=5
    
    #Flamethrower Constructor
    def __init__(self, screen, sound, level, id, mouse_pos, player_pos):
        self.flamethrower=[]
        sound.fire.play()
        self.id=id
        self.screen=screen
        self.frame=0
        self.angle = getAngleBetweenPoints(player_pos[0], mouse_pos[1], mouse_pos[0], player_pos[1])
        self.Flamethrower=[]
        for i in range(1,13):
            name_str = "images/animations/Flamethrower/" + str(i) + ".png"
            self.flamethrower.append(pygame.transform.flip(pygame.transform.scale2x(pygame.image.load(name_str)).convert_alpha(), False, True))
            if mouse_pos[0] > player_pos[0]:
                self.flamethrower[i-1] = pygame.transform.flip(self.flamethrower[i-1], False, True)
            self.flamethrower[i-1] = pygame.transform.rotate(self.flamethrower[i-1],self.angle)
        self.pos=(player_pos[0]-55,player_pos[1]-35)
        self.level=level
        self.sounds=sound
        self.hbox = Rect((player_pos[0]+55,player_pos[1]+45),(110 , 70))
        
    def hitbox(self):
        self.hbox=Rect((self.pos[0]+55, self.pos[1]+45), (110,70))
     
    
    def getType(self):
        return "flamethrower"
    def isDead(self):
        dead=(self.pos[0]>1280 or self.pos[0]<0 or self.pos[1]>720 or self.pos[1]<0) 
        if self.frame >= len(self.flamethrower)*5 -1:
            return True
        return dead or self.died

    def draw(self):
        self.hitbox()
        return (self.flamethrower[((int(self.frame)/5)%len(self.flamethrower))],(self.pos[0], self.pos[1]))

    def getAnimation(self):
        if self.animation==1:
            return self.fired_sprites[(self.anim_frames/10)%len(self.fired_sprites)]
        elif self.animation==2:
            return self.destruct_sprite[(self.anim_frames/10)%len(self.destruct_sprite)]

    
    def toString(self):
        return "%d,%d,%d" % (self.pos[0],self.pos[1],self.angle)

    def getPos(self):
        return self.pos