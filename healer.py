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
    reskin="ae98e2"
    #reskin="original"
    
    def __init__(self, screen, sound, level, name, team):
        self.screen=screen
        self.pos=((int(team)*1200+10), 64)
        self.stand_sprites = []
        for i in range(1,6):
            string = "images/animations/healer/" + self.reskin + "/healer_idle_" + str(i) + ".png"
            self.stand_sprites.append(pygame.transform.scale2x(pygame.image.load(string)).convert_alpha())
        self.slide_sprite = [pygame.transform.scale2x(pygame.image.load("images/animations/healer/" + self.reskin + "/healer_slide.png")).convert_alpha()]
        self.walk_sprites = []
        for i in range(1,6):
            string = "images/animations/healer/" + self.reskin + "/healer_walk_" + str(i) + ".png"
            self.walk_sprites.append(pygame.transform.scale2x(pygame.image.load(string)).convert_alpha())
        self.jump_sprites = []
        for i in range(1,13):
            string = "images/animations/healer/" + self.reskin + "/healer_jump_" + str(i) + ".png"
            self.jump_sprites.append(pygame.transform.scale2x(pygame.image.load(string)).convert_alpha())
        self.fall_sprites = []
        for i in range(1,6):
            string = "images/animations/healer/" + self.reskin + "/healer_idle_" + str(i) + ".png"
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
        
        
    
        
    
    
        