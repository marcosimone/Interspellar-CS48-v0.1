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
    def __init__(self, screen, sound, level, id, mouse_pos, player_pos):
        sound.fire.play()
        self.screen=screen
        self.frame=0
        self.id=id
        self.angle = getAngleBetweenPoints(player_pos[0], mouse_pos[1], mouse_pos[0], player_pos[1]+32)
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
    def setDamage(self, dmg):
        self.damage = dmg
    def setSpeed(self, spd):
        self.speed = spd
    def draw(self):
        self.hitbox()
        return (self.fireball[((int(self.frame)/5)%len(self.fireball))],(self.pos[0], self.pos[1]))
        
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
        
    def getType(self):
        return "fireball"
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
#b(ullet):  ("b", id, (posx, posy, type) , angle, sender)  
class enemyBullet(Bullet):
    player="enemy"
    frame=0
    type = "fireball"
    def __init__(self, screen, sound, level, id, pos, angle, sender, btype):
        self.id=id
        self.pos=pos
        sound.fire.play()
        self.screen=screen
        self.angle = angle
        self.sender= sender
        self.fireball=[]
        self.type = btype
        if(btype == "fireball"):
            for i in range(1,15):
                name_str = "images/animations/fireball/fireball_" + str(i) + ".png"
                self.fireball.append(pygame.transform.scale2x(pygame.image.load(name_str)).convert_alpha())
                if self.angle + 90 > 180:
                    self.fireball[i-1] = pygame.transform.flip(self.fireball[i-1], False, True)
                self.fireball[i-1] = pygame.transform.rotate(self.fireball[i-1],self.angle)
            self.setDamage(75)
            self.setSpeed(10)
            self.hbox = Rect((pos[0]+3,pos[1]+8),(64, 16))
        elif(btype == "flamethrower"):
            for i in range(1,13):
                name_str = "images/animations/Flamethrower/" + str(i) + ".png"
                self.fireball.append(pygame.transform.scale2x(pygame.image.load(name_str)).convert_alpha())
                if self.angle + 90 > 180:
                    self.fireball[i-1] = pygame.transform.flip(self.fireball[i-1], False, True)
                self.fireball[i-1] = pygame.transform.rotate(self.fireball[i-1],self.angle)
            self.setDamage(150)
            self.setSpeed(5)
            self.hbox = Rect((pos[0],pos[1]+55),(110, 70))
        elif(btype == "snipe"):
            for i in range(1,8):
                name_str = "images/animations/snipe/void_laser_" + str(i) + ".png"
                self.fireball.append(pygame.transform.scale2x(pygame.image.load(name_str)).convert_alpha())
                self.fireball[i-1] = pygame.transform.flip(self.fireball[i-1], True, False)
                if self.angle + 90 > 180:
                    self.fireball[i-1] = pygame.transform.flip(self.fireball[i-1], False, True)
                self.fireball[i-1] = pygame.transform.rotate(self.fireball[i-1],self.angle)
            self.setDamage(120)
            self.setSpeed(20)
            self.hbox = Rect((pos[0]+3,pos[1]+8),(32, 16))
        elif(btype == "wimpy"):
            for i in range(1,15):
                name_str = "images/animations/fireball/fireball_" + str(i) + ".png"
                self.fireball.append(pygame.image.load(name_str).convert_alpha())
                if self.angle + 90 > 180:
                    self.fireball[i-1] = pygame.transform.flip(self.fireball[i-1], False, True)
                self.fireball[i-1] = pygame.transform.rotate(self.fireball[i-1],self.angle)
            self.setDamage(50)
            self.setSpeed(8)
            self.hbox = Rect((pos[0]+3,pos[1]+8),(8, 8))
        elif(btype == "heal"):
            for i in range(1,11):
                name_str = "images/animations/heal_beam/heal_" + str(i) + ".png"
                self.fireball.append(pygame.transform.scale2x(pygame.image.load(name_str)).convert_alpha())
                if self.angle + 90 > 180:
                    self.fireball[i-1] = pygame.transform.flip(self.fireball[i-1], False, True)
                self.fireball[i-1] = pygame.transform.rotate(self.fireball[i-1],self.angle)
            self.setDamage(-100)
            self.setSpeed(8)
            self.hbox = Rect((pos[0]+3,pos[1]+8),(32, 16))
        self.pos=pos
        
        self.level=level
        self.sounds=sound
    def isDead(self):
        dead=(self.pos[0]>1280 or self.pos[0]<0 or self.pos[1]>720 or self.pos[1]<0) 
        if self.frame >= len(self.fireball)*5 -1:
            return True
        if self.type != "flamethrower":
            return Bullet.isDead(self)
        return dead or self.died
    