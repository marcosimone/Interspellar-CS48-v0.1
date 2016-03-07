import pygame, sys, socket
from pygame.locals import *
from array import array
from math import *
from soundboard import soundboard
from player import Player
import bullet
from heal_beam import Heal
from wimpy import Wimpy

class Healer(Player):
    
    anim_frames=0
    animation=0
    direction=0
    jump=0
    reskin="127800"
    #reskin="ae98e2"
    #reskin="original"
    
    def __init__(self, screen, sound, level, name, team):
        self.screen=screen
        if team == "0":
            self.reskin = "ae98e2"
        else:
            self.reskin = "127800"
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
    def fullRegCooldown(self):
        return 80
    def fullSpecCooldown(self):
        return 300
    
    def activateSpecial(self, screen, sounds, level, mouse_pos, sock):
        beam = Heal(screen, sounds, level, mouse_pos, self.getPos())
        return beam
            
    def activateRegular(self, screen, sounds, level, mouse_pos, sock):
        return Wimpy(screen, sounds, level, mouse_pos, self.getPos())
    
    def update(self, inputs, bullets, server):
        Player.update(self,inputs, bullets, server)
        
    def getAnimation(self):
        if self.animation==0:
            return self.stand_sprites[(int(self.anim_frame)/10)%len(self.stand_sprites)]
        elif self.animation==1:
            return self.walk_sprites[(int(self.anim_frame)/10)%len(self.walk_sprites)]
        elif self.animation==2:
            return self.jump_sprites[(int(self.jump)/6)%len(self.jump_sprites)]
        elif self.animation==3:
            return self.fall_sprites[(int(self.anim_frame)/10)%len(self.fall_sprites)]
        elif self.animation==4:
            return self.slide_sprite[0]
        elif self.animation==5:
            return self.spec_sprites[(int(self.anim_frame)/5)%len(self.spec_sprites)]
        
    
        
    
    
        