import pygame, sys, socket
from pygame.locals import *
from array import array
from math import *
from soundboard import soundboard
from player import Player
from bullet import Bullet
from flamethrower import Flamethrower

class DankWizard(Player):
    
    anim_frames=0
    animation=0
    direction=0
    jump=0
    color=""
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
        if team == "0":
            self.color="460099"
        else:
            self.color="004c00"
        self.pos=((int(team)*1200+10), 64)
        self.stand_sprites = [pygame.transform.scale2x(pygame.image.load("images/animations/dankwiz/" +self.color+ "/wizard.png")).convert_alpha()]
        self.slide_sprite = [pygame.transform.scale2x(pygame.image.load("images/animations/dankwiz/" +self.color+ "/wiz_slide.png")).convert_alpha()]
        self.walk_sprites = []
        for i in range(1,6):
            string = "images/animations/dankwiz/" +self.color+ "/wiz_walk_" + str(i) + ".png"
            self.walk_sprites.append(pygame.transform.scale2x(pygame.image.load(string)).convert_alpha())
        self.jump_sprites = []
        for i in range(1,13):
            string = "images/animations/dankwiz/" +self.color+ "/wiz_jump_" + str(i) + ".png"
            self.jump_sprites.append(pygame.transform.scale2x(pygame.image.load(string)).convert_alpha())
        self.fall_sprites = []
        for i in range(1,7):
            string = "images/animations/dankwiz/" +self.color+ "/wiz_fall_" + str(i) + ".png"
            self.fall_sprites.append(pygame.transform.scale2x(pygame.image.load(string)).convert_alpha())
        self.name=name
        self.team=team
        self.level=level
        self.sounds=sound
    
    
    def fullRegCooldown(self):
        return 80
    def fullSpecCooldown(self):
        return 250
        
    def activateRegular(self, screen, sounds, level, id, mouse_pos):
        return Bullet(screen, sounds, level, id, mouse_pos, self.getPos())

    def activateSpecial(self,screen,sounds,level,id ,mouse_pos):
        return Flamethrower(screen,sounds,level,id, mouse_pos,self.getPos())
 
            
    def update(self, inputs, bullets, server):
        Player.update(self,inputs, bullets, server)
        
        
    def getSpeed(self):
        return 4.5