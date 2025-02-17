import pygame, sys, socket
from pygame.locals import *
from array import array
from math import *
from soundboard import soundboard
from bullet import *
import tools


"""Snipe is a fast moving shot that traverses 
   the entire map and does significant damage"""

class Snipe(Bullet):
    anim_frames = 0
    aniimation = 0
    speed=20
    damage=120
    
    
    #Snipe Constructor
    def __init__(self, screen, sound, level, id, mouse_pos, player_pos):
        self.snipe=[]
        self.id=id
        sound.fire.play()
        self.screen=screen
        self.frame=0
        self.angle = getAngleBetweenPoints(player_pos[0], mouse_pos[1], mouse_pos[0], player_pos[1])
        for i in range(1,8):
            name_str = "resources/images/animations/snipe/void_laser_" + str(i) + ".png"
            self.snipe.append(pygame.transform.scale2x(pygame.image.load(tools.resource_path(name_str))).convert_alpha())
            self.snipe[i-1] = pygame.transform.flip(self.snipe[i-1], True, False)
            if mouse_pos[0] > player_pos[0]:
                self.snipe[i-1] = pygame.transform.flip(self.snipe[i-1], False, True)
            self.snipe[i-1] = pygame.transform.rotate(self.snipe[i-1],self.angle)
        self.pos=(player_pos[0]-16,player_pos[1]-16)
        self.level=level
        self.sounds=sound
        self.hbox = Rect((player_pos[0],player_pos[1]),(64 , 32))
        
    def hitbox(self):
        self.hbox=Rect((self.pos[0], self.pos[1]), (64,32))
        
    def getType(self):
        return "snipe"
    
    def isDead(self):
        dead=(self.pos[0]>1280 or self.pos[0]<0 or self.pos[1]>720 or self.pos[1]<0) 
        for l in self.level:
            if l.collidepoint(self.hbox.center):
                return True
        return dead or self.died

    def draw(self):
        self.hitbox()
        return (self.snipe[((int(self.frame)/5)%len(self.snipe))],(self.pos[0], self.pos[1]))

    def getAnimation(self):
        if self.animation==1:
            return self.fired_sprites[(self.anim_frames/10)%len(seld.fired_sprites)]
        elif self.animation==2:
            return self.destruct_sprite[(self.anim_frames/10)%len(self.destruct_sprite)]

     
    def toString(self):
        return "%d,%d,%d" % (self.pos[0],self.pos[1],self.angle)

    def getPos(self):
        return self.pos
