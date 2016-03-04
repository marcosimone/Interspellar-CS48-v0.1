import pygame, sys, socket
from pygame.locals import *
from array import array
from math import *
from soundboard import soundboard
from player import Player
from bullet import *
import bullet

class DarkWizard(Player):
    
    anim_frames=0
    animation=0
    direction=0
    jump=0
    color="original"
    tp_loc=(0,0)
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
            string = "images/animations/darkwiz/dark_tp_" + str(i) + ".png"
            self.spec_sprites.append(pygame.transform.scale2x(pygame.image.load(string)).convert_alpha())
            
            
        
        self.level=level
        self.sounds=sound
    
        
    
    def fullRegCooldown(self):
        return 30
    def fullSpecCooldown(self):
        return 200
        
    
    def activateRegular(self, screen, sounds, level, mouse_pos, sock):
        return Bullet(screen, sounds, level, mouse_pos, self.getPos())
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


    def update(self, inputs, bullets):
        Player.update(self,inputs, bullets)
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
    def draw(self):
        if self.direction == 0:
            return (self.getAnimation(), self.getPos())
        else:
            return (pygame.transform.flip(self.getAnimation(), True, False), self.getPos())
        
        
    
        
