import pygame
class soundboard:
	
	def __init__(self):
		self.click = pygame.mixer.Sound("sound/click.wav")
		self.fire = pygame.mixer.Sound("sound/fire.wav")
		self.explode = pygame.mixer.Sound("sound/explosion.wav")