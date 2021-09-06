import pygame

class Cell:
	traversable = True

	def __init__(self, x, y, width, height, fill, border):
		self.x = x
		self.y = y
		self.width = width
		self.height = height

		self.fill = fill
		self.border = border

		self.rect = pygame.Rect(self.x, self.y, self.width, self.height)

		self.updated = True
	

	def draw(self, window):
		if not self.updated:
			return

		pygame.Surface.fill(window, self.fill, self.rect)
		pygame.draw.rect(window, self.border, self.rect, 1)

		self.updated = False
