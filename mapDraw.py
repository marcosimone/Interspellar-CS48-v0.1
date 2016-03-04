import pygame, sys, socket
from pygame.locals import *
from array import array
from math import *

class Map: 
	listOfTexturedSurfaces = [] 
	listOfLevelRects = [] 
	mapList = []

	texture0 = []
	texture1 = []
	
	#map 0 is vertical-combat based Enclosed walls for wall jumping, main center area, walls with holes 
	map0 = [Rect((0,0),(50,720)), Rect((1230,0),(50,720)), Rect((200,470),(75,250)), Rect((1005,470),(75,250)), 
			Rect((200,150),(75,200)), Rect((1005, 150),(75,200)), Rect((440,500),(400,100)), 
			Rect((440,200),(75,200)), Rect((765,200),(75,200)), Rect((590,275),(100,50)) ]
	#map 1 has a very open top half with a close quarters lower map with a u-shaped platform 
	map1 = [Rect((0,275),(250,50)), Rect((1030,275),(250,50)), Rect((0,325),(50,395)), Rect((1230,325),(50,395)),
			Rect((955,475),(150,40)), Rect((175,475),(150,40)), Rect((440,550),(400,60)), Rect((440,490),(75,60)), 
			Rect((765,490),(75,60)), Rect((390,250),(500,75)) ]
	#map 2 is very open, with a small enclosed space at the bottom, few platforms and walls up top, looks like a face
	map2 = [Rect((0,520),(300,200)), Rect((980,520),(300,200)), Rect((440,540),(400,50)), Rect((615,200),(50,200)),
			Rect((220,275),(200,50)), Rect((840,275),(200,50)), Rect((0,200),(25,200)), Rect((1255,200),(25,200)) ]
	#map 3 focuses on a more horizontal combat layout, there are 4 lanes created by two very long platforms
	map3 = [Rect((0,320),(50,400)), Rect((1230,320),(50,400)), Rect((0,670),(250,50)), Rect((1030,670),(250,50)), 
			Rect((240,400),(800,75)), Rect((290,200),(700,75)), Rect((0,320),(100,50)), Rect((1180,320),(100,50)) ]
	mapList = [map0, map1, map2, map3]
	
	#go through rectangles, create surfaces to append to toDraw_background 
	#these surfaces are the same size as the rectangles, textures mapped onto them 
	def __init__(self, id):
		self.texture0 = pygame.image.load("images/textures/stoner.png").convert()
		self.texture1 = pygame.image.load("images/textures/brownTexture.png").convert()
		textureList = [self.texture0, self.texture1]

		self.listOfLevelRects = self.mapList[id] 
		texture = textureList[id]
		
		for plat in self.listOfLevelRects:
			newSurface = pygame.Surface((plat.width,plat.height))
			numberOfTexturesX = (plat.width/texture.get_width()) + 1    
			numberOfTexturesY = (plat.height/texture.get_height()) + 1    
			destVarX = 0
			for i in range(0,numberOfTexturesX):
				destVarY = 0
				for j in range(0,numberOfTexturesY):
					newSurface.blit(texture, (destVarX,destVarY))
					destVarY = destVarY + texture.get_height()
				destVarX = destVarX + texture.get_width()
			self.listOfTexturedSurfaces.append(newSurface)
			#pygame.image.save(newSurface, 'test.png')

	def getTextures(self): 
		return self.listOfTexturedSurfaces

	def getLevel(self): 
		return self.listOfLevelRects
