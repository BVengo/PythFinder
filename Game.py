import pygame
from pygame.locals import *
import sys
from Grid import Grid
from Color import Color
from AStarAlgorithm import AStarAlgorithm
from StartCell import StartCell
from EndCell import EndCell

class Game:

	def __init__(self, windowWidth, windowHeight):
		pygame.init()

		self.window = pygame.display.set_mode((windowWidth, windowHeight))
		self.window.fill(Color.WHITE)

		self.grid = Grid(0, 0, windowWidth, windowHeight, 20, 20)

		pygame.display.flip()


	def run(self):
		while True:
			self.handleInput()
			self.draw()
			pygame.display.update()


	def handleInput(self):
		for event in pygame.event.get():
			if event.type == pygame.MOUSEBUTTONDOWN:
				pos = pygame.mouse.get_pos()

				if event.button == 1:
					self.grid.handle_lclick(pos)
				elif event.button == 3:
					self.grid.handle_rclick(pos)
			elif event.type == pygame.KEYDOWN:
				if event.key == K_ESCAPE:
					self.grid.clear()
				if event.key == K_SPACE:
					self.grid.reset()
					self.runPathFinder()						
			elif event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()
					

	def draw(self):
		self.grid.draw(self.window)

	
	def runPathFinder(self):
		if self.grid.startCell != None and self.grid.endCell != None:
			algorithm = AStarAlgorithm(self.grid, self.grid.startCell, self.grid.endCell)
			pathEnd = algorithm.find_path()

			if pathEnd is None:
				print('No path available between start and end nodes.')
				return

			pathNode = pathEnd

			while pathNode != None:
				if type(pathNode.cell) != StartCell and type(pathNode.cell) != EndCell:
					pathNode.cell.fill = Color.YELLOW
					pathNode.cell.updated = True

				pathNode = pathNode.parent