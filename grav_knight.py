import pygame, sys, socket
from pygame.locals import *
from array import array
from math import *
from soundboard import soundboard
from player import Player
import bullet

class GravityKnight(Player):
    
    anim_frames=0
    animation=0
    direction=0
    jump=0
    color="original"
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
        
        self.level=level
        self.sounds=sound
    
        
    
    def fullRegCooldown(self):
        return 30
    def fullSpecCooldown(self):
        return 80
        
    def activateSpecial(self, mouse_pos, player_pos, sock):
        
        rad=radians(bullet.getAngleBetweenPoints(mouse_pos[0], mouse_pos[1], player_pos[0], player_pos[1]))
        body=Rect((self.pos[0]-32,self.pos[1]-64), (64,64))
        
        for i in range(0,20):
            self.velocity=0
            self.attemptMove(rad, 20)        
        return
        
    def attemptMove(self, rad, dist):
        xpos=self.pos[0]
        ypos=self.pos[1]
        nextLoc=Rect((self.pos[0]-(dist*cos(rad)) - 32, self.pos[1] - (dist*sin(rad)) - 64), (64,64))
        if nextLoc.collidelist(self.level) == -1:
            self.pos=(self.pos[0]-(dist*cos(rad)), self.pos[1]-(dist*sin(rad)))
        
    def update(self, inputs, bullets):
        Player.update(self,inputs, bullets)

    def getSpeed(self):
        return 4
    def draw(self):
        if self.direction == 0:
            return (self.getAnimation(), self.getPos())
        else:
            return (pygame.transform.flip(self.getAnimation(), True, False), self.getPos())
        
        
    
        