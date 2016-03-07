import pygame, sys, socket
from pygame.locals import *
from array import array
from math import *
from soundboard import soundboard
from player import Player
import bullet
from bullet import Bullet
from Snipe import Snipe


class DarkWizard(Player):
    
    anim_frames=0
    animation=0
    direction=0
    jump=0

    #color="original"
    color=""
    tp_loc=(0,0)
    #COLORS SUPPORTED SO FAR:
    # 004c00 : green
    # 0066cc : light blue
    # 460099 : purple
    # 800000 : red
    # e5e600 : yellow
    # 000080 : blue
    # cc5200 : orange
    
    def __init__(self, screen, sound, level, name, team):
        self.screen=screen
        if team=="0":
            self.color="460099"
        else:
            self.color="004c00"
        self.stand_sprites = []
        for i in range(1,6):
            string = "images/animations/darkwiz/" + self.color + "/dark_idle_" + str(i) + ".png"
            self.stand_sprites.append(pygame.transform.scale2x(pygame.image.load(string)).convert_alpha())
        self.slide_sprite = [pygame.transform.scale2x(pygame.image.load("images/animations/darkwiz/" + self.color + "/dark_slide.png")).convert_alpha()]
        self.walk_sprites = []
        for i in range(1,6):
            string = "images/animations/darkwiz/" + self.color + "/dark_walk_" + str(i) + ".png"
            self.walk_sprites.append(pygame.transform.scale2x(pygame.image.load(string)).convert_alpha())
        self.jump_sprites = []
        for i in range(1,13):
            string = "images/animations/darkwiz/" + self.color + "/dark_jump_" + str(i) + ".png"
            self.jump_sprites.append(pygame.transform.scale2x(pygame.image.load(string)).convert_alpha())
        self.fall_sprites = []
        for i in range(1,6):
            string = "images/animations/darkwiz/" + self.color + "/dark_fall_" + str(i) + ".png"
            self.fall_sprites.append(pygame.transform.scale2x(pygame.image.load(string)).convert_alpha())
        self.spec_sprites = []
        for i in range(1,5):
            string = "images/animations/darkwiz/" +self.color+"/dark_tp_" + str(i) + ".png"
            self.spec_sprites.append(pygame.transform.scale2x(pygame.image.load(string)).convert_alpha())
        self.pos=((int(team)*1200+10), 64)
        self.name=name
        self.team=team
        self.level=level
        self.sounds=sound
    
        
    
    def fullRegCooldown(self):
        return 80
    def fullSpecCooldown(self):
        return 200
        
    
    def activateRegular(self, screen, sounds, level, mouse_pos, sock):
        return Snipe(screen, sounds, level, mouse_pos, self.getPos())
    
    def activateSpecial(self, screen, sounds, level, mouse_pos, sock):
        while sqrt((mouse_pos[0]-self.pos[0])**2 + (mouse_pos[1]-self.pos[1])**2) > 400:
            angle = bullet.getAngleBetweenPoints(mouse_pos[0], mouse_pos[1], self.pos[0], self.pos[1])
            rad = radians(angle)
            mouse_pos = (mouse_pos[0] + 5*cos(rad), mouse_pos[1] + 5*sin(rad))
            

            
        nextLoc=Rect((mouse_pos[0] - 32, mouse_pos[1] - 64), (64,64))
        if nextLoc.collidelist(self.level) == -1:
            self.tp_loc=mouse_pos
        else:
            self.spec_cooldown = 0
            return None


    def update(self, inputs, bullets, server):
        Player.update(self,inputs, bullets, server)
        if self.tp_loc[0] != 0 and self.tp_loc[1] != 0:
            self.animation = 5
            self.spec_frame +=1
            if self.spec_frame >= 20:
                self.pos = self.tp_loc
                self.tp_loc = (0,0)
                
        else:
            self.spec_frame=-1

    def getSpeed(self):
        return 4
    
        
        
    
        
