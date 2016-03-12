import pygame
import tools
class soundboard:
	
	def __init__(self):
		self.click = pygame.mixer.Sound(tools.resource_path("resources/sound/click.wav"))
		self.fire = pygame.mixer.Sound(tools.resource_path("resources/sound/fire.wav"))
		self.explode = pygame.mixer.Sound(tools.resource_path("resources/sound/explosion.wav"))