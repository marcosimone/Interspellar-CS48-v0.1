import pygame, sys, socket
from pygame.locals import *
from array import array
from math import *
from soundboard import soundboard

    
class Player:
    health=1000
    max_health=1000
    velocity=0
    xvelocity=0
    anim_frame=0
    spec_frame=0
    reg_cooldown=20
    spec_cooldown=60

    def __init__(self, screen, sound, level, player_pos):
        self.screen=screen
        self.image = [pygame.transform.scale2x(pygame.image.load("images/animations/floating_blood_1.png").convert_alpha()),pygame.transform.scale2x(pygame.image.load("images/animations/floating_blood_2.png").convert_alpha())]
        self.pos=player_pos
        self.level=level
        self.sounds=sound
        self.reg_cooldown = 200
    
    def getCurrentHealth(self):
        return self.health
        
    def getMaxHealth(self):
        return self.max_health
        
    def damage(self, damage):
        self.health = self.health - damage
    
    def heal(self, heal):
        self.health = self.health + heal
        if self.health > self.max_health:
            self.health = self.max_health
        
    def draw(self):
        return (self.image[(self.anim_frame/30)%2], self.getPos())
    
    def isDead(self):
        return (self.health<=0)
    
    def getPos(self):
        return (self.pos[0]-32, self.pos[1]-64)
    
    def setPos(self, pos):
        self.pos=(pos[0]+32,pos[1]+64)
    def getRegCooldown(self):
        return self.reg_cooldown
    def fullRegCooldown(self):
        return 200
    def setRegCooldown(self, cool):
        self.reg_cooldown = cool;
    def getSpecCooldown(self):
        return self.spec_cooldown
    def fullSpecCooldown(self):
        return 60
    def setSpecCooldown(self, cool):
        self.spec_cooldown = cool;
        
    def activateSpecial(self, mouse_pos, player_pos, sock):
        return
    
   
        
    def update(self, inputs, bullets):
        body=Rect((self.pos[0]-32,self.pos[1]-64), (64,64))
        xpos=self.pos[0]
        ypos=self.pos[1]

        self.reg_cooldown = self.reg_cooldown - 1/(pygame.time.Clock().get_fps()+1)
        self.spec_cooldown = self.spec_cooldown - 1/(pygame.time.Clock().get_fps()+1)

        if self.reg_cooldown < 0:
            self.reg_cooldown = 0
        if self.spec_cooldown < 0:
            self.spec_cooldown = 0

        
        for bullet in bullets:
            if body.collidepoint(bullet.getPos()) and (bullet.player!="me"):
                bullet.selfDestruct()
                self.health-=100
                print self.health
                if isDead():
                    sys.exit()
        if inputs[1]==1:
            self.direction=1
        elif inputs[3]==1:
            self.direction=0
        
        col_index=body.collidelist(self.level)
        if self.velocity < -15:
            self.velocity =-15
            
        if inputs[0] and self.jump==0:
            self.jump=1
        if col_index!=-1:
            plat=self.level[col_index]
            
            if fabs(body.bottom-plat.top)<17:
                self.jump=0
                self.animation=0
                if inputs[1]==1 or inputs[3]==1:
                    self.animation=1
                self.velocity=0
                if inputs[0]:
                    ypos=plat.top-10
                    self.velocity=15
                    
            if fabs(body.top-plat.bottom)<12:
                self.velocity=-1.0
                self.animation=3
                
            
            elif body.bottom>plat.top-3 and body.top<plat.bottom+3:
                if fabs(body.right-plat.left)<10:
                    self.animation=4
                    self.jump=0
                    if self.velocity > 5:
                        self.velocity-=1.5
                    else:
                        self.velocity-=0.1
                    if self.velocity < -5:
                        self.velocity = -5
                    xpos=plat.left-32
                    if inputs[0]:
                        self.velocity = 10
                        self.xvelocity = -7
                        
                elif fabs(body.left-plat.right)<10:
                    self.animation=4
                    self.jump=0
                    if self.velocity > 5:
                        self.velocity-=1.5
                    else:
                        self.velocity-=0.1
                    if self.velocity < -5:
                        self.velocity = -5
                    xpos=plat.right+32
                    if inputs[0]:
                        self.velocity = 10
                        self.xvelocity = 7
                        
        else:
            if ypos <=32:
                self.velocity=-1
            if ypos < 720:
                self.animation=3
                self.velocity-=.5
            else:
                self.animation=0
                if inputs[1]==1 or inputs[3]==1:
                    self.animation=1
                if inputs[0]:
                    self.velocity=15
                else:
                    self.velocity=0
                self.jump=0
            if self.jump > 0:
                self.animation=2
                self.jump+=1
            if self.jump >30:
                self.jump=-1
        ypos=ypos-self.velocity
        xpos=xpos+self.xvelocity
        if self.xvelocity > 0:
            self.xvelocity-=0.4
        if self.xvelocity < 0:
            self.xvelocity+=0.4
        if fabs(self.xvelocity) < 0.5:
            self.xvelocity = 0
        if inputs[1]:
            xpos-=self.getSpeed()
        if inputs[3]:
            xpos+=self.getSpeed()
        if xpos < 32:
            xpos=32
        if xpos > 1248:
            xpos=1248
        if ypos > 720:
            ypos=720
        self.pos=(xpos, ypos)
        self .anim_frame+=1
        if self .anim_frame==360:
            self .anim_frame=0
        return
     
    def getSpeed(self):
        return 3
    
    def getAnimation(self):
        if self.animation==0:
            return self.stand_sprites[(self.anim_frame/10)%len(self.stand_sprites)]
        elif self.animation==1:
            return self.walk_sprites[(self.anim_frame/10)%len(self.walk_sprites)]
        elif self.animation==2:
            return self.jump_sprites[(self.jump/3)%len(self.jump_sprites)]
        elif self.animation==3:
            return self.fall_sprites[(self.anim_frame/10)%len(self.fall_sprites)]
        elif self.animation==4:
            return self.slide_sprite[0]
        elif self.animation==5:
            return self.spec_sprites[(self.spec_frame/5)%len(self.spec_sprites)]
