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
    color="004c00"
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
            string = "images/animations/healer/healer_idle_" + str(i) + ".png"
            self.stand_sprites.append(pygame.transform.scale2x(pygame.image.load(string)).convert_alpha())
        self.slide_sprite = [pygame.transform.scale2x(pygame.image.load("images/animations/healer/healer_slide.png")).convert_alpha()]
        self.walk_sprites = []
        for i in range(1,6):
            string = "images/animations/healer/healer_walk_" + str(i) + ".png"
            self.walk_sprites.append(pygame.transform.scale2x(pygame.image.load(string)).convert_alpha())
        self.jump_sprites = []
        for i in range(1,13):
            string = "images/animations/healer/healer_jump_" + str(i) + ".png"
            self.jump_sprites.append(pygame.transform.scale2x(pygame.image.load(string)).convert_alpha())
        self.fall_sprites = []
        for i in range(1,6):
            string = "images/animations/healer/healer_idle_" + str(i) + ".png"
            self.fall_sprites.append(pygame.transform.scale2x(pygame.image.load(string)).convert_alpha())
        
        self.level=level
        self.sounds=sound
    
        
    def update(self, inputs, bullets):
        Player.update(self,inputs, bullets)
        
        
    def draw(self):
        if self.direction == 0:
            return (self.getAnimation(), self.getPos())
        else:
            return (pygame.transform.flip(self.getAnimation(), True, False), self.getPos())
        
    
    
        