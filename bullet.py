import pygame, sys, socket
from pygame.locals import *
from array import array
from math import *
from soundboard import soundboard
def angle_trunc(a):
    while a < 0.0:
        a += pi * 2
    return a*(360/(2*pi))

def getAngleBetweenPoints(x_orig, y_orig, x_landmark, y_landmark):
    deltaY = y_landmark - y_orig
    deltaX = x_landmark - x_orig
    return angle_trunc(atan2(deltaY, deltaX))

class Bullet:


    speed=10
    fps=60
    died=False
    player="me"
    damage=10
    id=0 #will determine speed and damage
    def __init__(self, screen, sound, level, mouse_pos, player_pos):
        sound.fire.play()
        self.screen=screen
        self.frame=0
        self.angle = getAngleBetweenPoints(player_pos[0], mouse_pos[1], mouse_pos[0], player_pos[1])
        self.fireball=[]
        for i in range(1,15):
            name_str = "images/animations/fireball/fireball_" + str(i) + ".png"
            self.fireball.append(pygame.transform.scale2x(pygame.image.load(name_str)).convert_alpha())
        #self.image = pygame.transform.rotate(image,-45)
            self.fireball[i-1] = pygame.transform.rotate(self.fireball[i-1],self.angle)
        self.pos=(player_pos[0],player_pos[1])
        self.hbox = Rect((player_pos[0]+3,player_pos[1]+16),(1 , 32))
        self.level=level
        self.sounds=sound
    
    def hitbox(self):
        self.hbox=Rect((self.pos[0], self.pos[1]+16), (64,32))
        return
    
    def draw(self):
        self.hitbox()
        return (self.fireball[((int(self.frame)/5)%14)],(self.pos[0], self.pos[1]))
        
    def isDead(self):
        dead=(self.pos[0]>1280 or self.pos[0]<0 or self.pos[1]>720 or self.pos[1]<0) 
        if self.frame >= len(self.fireball)*5 -1:
            return True
        #for ob in self.level:
        #    if ob.colliderect(self.hbox):
        #        return True.
        if self.hbox.collidelist(self.level) == -1:
            return False
        else:
            return True
        return dead or self.died
        
    def selfDestruct(self):
        self.died=True
        
    
    def update(self):
        self.frame+=60/float(self.fps)
        rad=radians(self.angle)
        self.pos=(self.pos[0]+(self.getSpeed()*cos(rad)), self.pos[1]-(self.getSpeed()*sin(rad)))
        self.hbox=(self.pos[0]+(self.getSpeed()*cos(rad)), self.pos[1]-(self.getSpeed()*sin(rad)))
    
    def setFPS(self, FPS):
        self.fps = float(FPS)
    def getSpeed(self):
        return self.speed * 60 / float(self.fps)
    def toString(self):
        return "%d,%d,%d" % (self.pos[0],self.pos[1],self.angle)
        
    def getPos(self):
        return self.pos
#b(ullet):  ("b", id, type, (posx, posy) , angle, sender)  
class enemyBullet(Bullet):
    player="enemy"
    frame=0
    def __init__(self, screen, sound, level, id, pos, angle, sender):
        self.id=id
        self.pos=pos
        sound.fire.play()
        self.screen=screen
        self.angle = angle
        self.sender= sender
        self.fireball=[]
        for i in range(1,15):
            name_str = "images/animations/fireball/fireball_" + str(i) + ".png"
            self.fireball.append(pygame.transform.scale2x(pygame.image.load(name_str)).convert_alpha())
        #self.image = pygame.transform.rotate(image,-45)
            self.fireball[i-1] = pygame.transform.rotate(self.fireball[i-1],self.angle)
        self.pos=pos
        self.hbox = Rect((pos[0]+3,pos[1]+16),(1 , 32))
        
        self.level=level
        self.sounds=sound
    
    