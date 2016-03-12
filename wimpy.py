import pygame, sys, socket
from pygame.locals import *
from array import array
from math import *
from soundboard import soundboard
from bullet import *
import tools


"""Wimpy is a cone of fire that has a set
   radius and cooldown time"""

class Wimpy(Bullet):
    anim_frames = 0
    aniimation = 0
    damage=50
    speed=10
    
    #Flamethrower Constructor
    def __init__(self, screen, sound, level, id, mouse_pos, player_pos):
        sound.fire.play()
        self.screen=screen
        self.frame=0
        self.id=id
        self.angle = getAngleBetweenPoints(player_pos[0], mouse_pos[1], mouse_pos[0], player_pos[1])
        self.wimpy=[]
        for i in range(1,15):
            name_str = "resources/images/animations/fireball/fireball_" + str(i) + ".png"
            self.wimpy.append(pygame.image.load(tools.resource_path(name_str)).convert_alpha())
            self.wimpy[i-1] = pygame.transform.rotate(self.wimpy[i-1],self.angle)
        self.pos=(player_pos[0]+8,player_pos[1]+16)
        self.level=level
        self.sounds=sound
        self.hbox = Rect((player_pos[0],player_pos[1]+8),(32 , 16))
        
    def hitbox(self):
        self.hbox=Rect((self.pos[0], self.pos[1]+8), (32,16))
        
    def getType(self):
        return "wimpy"
    
    def isDead(self):
        dead=(self.pos[0]>1280 or self.pos[0]<0 or self.pos[1]>720 or self.pos[1]<0) 
        if self.frame >= len(self.wimpy)*5 -1:
            return True
        for l in self.level:
            if l.collidepoint(self.hbox.center):
                return True
        return dead or self.died

    def draw(self):
        self.hitbox()
        return (self.wimpy[((int(self.frame)/5)%len(self.wimpy))],(self.pos[0], self.pos[1]))

    def getAnimation(self):
        if self.animation==1:
            return self.fired_sprites[(self.anim_frames/10)%len(self.fired_sprites)]
        elif self.animation==2:
            return self.destruct_sprite[(self.anim_frames/10)%len(self.destruct_sprite)]

    
    def toString(self):
        return "%d,%d,%d" % (self.pos[0],self.pos[1],self.angle)

    def getPos(self):
        return self.pos