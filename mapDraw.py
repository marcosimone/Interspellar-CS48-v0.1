import pygame, sys, socket
from pygame.locals import *
from array import array
from math import *

class Map: 
	listOfTexturedSurfaces = [] 
	listOfLevelRects = [] 
	mapList = []
	backgroundVar = []
	
	texture0 = []
	platText0 = []
	background0 = []
	texture1 = []
	platText1 = []
	background1 = []
	texture2 = []
	platText2 = []
	background2 = []
	texture3 = []
	platText3 = []
	background3 = []
	
	#map 0 is vertical-combat based Enclosed walls for wall jumping, main center area, walls with holes 
	map0 = [Rect((0,0),(50,720)), Rect((1230,0),(50,720)), Rect((200,470),(75,250)), Rect((1005,470),(75,250)), 
			Rect((200,150),(75,200)), Rect((1005, 150),(75,200)), Rect((440,500),(400,100)), 
			Rect((440,200),(75,200)), Rect((765,200),(75,200)), Rect((590,275),(100,50)) ]
	#map 1 has a very open top half with a close quarters lower map with a u-shaped platform 
	map1 = [Rect((0,275),(250,50)), Rect((1030,275),(250,50)), Rect((0,275),(50,445)), Rect((1230,275),(50,445)),
			Rect((955,475),(150,40)), Rect((175,475),(150,40)), Rect((440,550),(400,60)), Rect((440,490),(75,60)), 
			Rect((765,490),(75,60)), Rect((390,250),(500,75)) ]
	#map 2 is very open, with a small enclosed space at the bottom, few platforms and walls up top, looks like a face
	map2 = [Rect((0,520),(300,200)), Rect((980,520),(300,200)), Rect((440,540),(400,50)), Rect((615,200),(50,200)),
			Rect((220,275),(200,50)), Rect((840,275),(200,50)), Rect((0,200),(25,200)), Rect((1255,200),(25,200)) ]
	#map 3 focuses on a more horizontal combat layout, there are 4 lanes created by two very long platforms
	map3 = [Rect((0,320),(50,400)), Rect((1230,320),(50,400)), Rect((0,670),(250,50)), Rect((1030,670),(250,50)), 
			Rect((240,400),(800,75)), Rect((290,200),(700,75)), Rect((0,320),(100,50)), Rect((1180,320),(100,50)) ]
	mapList = [map0, map1, map2, map3]
	
	def __init__(self, id):
		self.texture0 = pygame.image.load("images/textures/snowCenter.png").convert()
		self.texture1 = pygame.image.load("images/textures/sandCenter.png").convert()
		self.texture2 = pygame.image.load("images/textures/grassCenter.png").convert()
		self.texture3 = pygame.image.load("images/textures/castleCenter.png").convert()
		textureList = [self.texture0, self.texture1, self.texture2, self.texture3]

		self.platText0 = pygame.image.load("images/textures/snowMid.png").convert_alpha()
		self.platText1 = pygame.image.load("images/textures/sandMid.png").convert_alpha() 
		self.platText2 = pygame.image.load("images/textures/grassMid.png").convert_alpha()
		self.platText3 = pygame.image.load("images/textures/castleMid.png").convert_alpha()
		platTextList = [self.platText0, self.platText1, self.platText2, self.platText3]

		self.background0 = pygame.transform.smoothscale(pygame.image.load("images/backgrounds/mountainBackground.png").convert(), (1280,720))
		self.background1 = pygame.transform.smoothscale(pygame.image.load("images/backgrounds/desertBackground.png").convert(), (1280,720))
		self.background2 = pygame.transform.smoothscale(pygame.image.load("images/backgrounds/forestBackground.png").convert(), (1280,720))
		self.background3 = pygame.transform.smoothscale(pygame.image.load("images/backgrounds/nightBackground.png").convert(), (1280,720))
		backgroundList = [self.background0, self.background1, self.background2, self.background3]

		self.backgroundVar = backgroundList[id]
		self.listOfLevelRects = self.mapList[id] 
		texture = textureList[id]
		platText = platTextList[id]
		
		for plat in self.listOfLevelRects:
			newSurface = pygame.Surface((plat.width,plat.height))
			newSurface.set_colorkey((0,0,0))

			destVarX = 0 
			destVarY = 0
			numberOfTexturesX = (plat.width/platText.get_width()) + 1 
			for i in range(0,numberOfTexturesX): 
				newSurface.blit(platText, (destVarX,destVarY))
				destVarX = destVarX + platText.get_width()

			numberOfTexturesX = (plat.width/texture.get_width()) + 1    
			numberOfTexturesY = (plat.height/texture.get_height()) + 1    
			destVarX = 0
			for i in range(0,numberOfTexturesX):
				destVarY = platText.get_height()
				for j in range(0,numberOfTexturesY):
					newSurface.blit(texture, (destVarX,destVarY))
					destVarY = destVarY + texture.get_height()
				destVarX = destVarX + texture.get_width()
			self.listOfTexturedSurfaces.append(newSurface)
			
	def getTextures(self): 
		return self.listOfTexturedSurfaces

	def getLevel(self): 
		return self.listOfLevelRects

	def getBackground(self): 
		return self.backgroundVar
