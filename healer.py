import pygame, sys, socket
from pygame.locals import *
from array import array
from math import *
from soundboard import soundboard
from player import Player
import bullet
from heal_beam import Heal

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
    
    def __init__(self, screen, sound, level, name, team):
        self.screen=screen
        self.pos=((int(team)*1200+10), 64)
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
        
        self.name=name
        self.team=team
        self.level=level
        self.sounds=sound
    
    
    def activateSpecial(self, screen, sounds, level, mouse_pos, sock):
        beam = Heal(screen, sounds, level, mouse_pos, self.getPos())
        return beam
            
    
    def update(self, inputs, bullets, server):
        Player.update(self,inputs, bullets, server)
        
        
    
        
    
    
        