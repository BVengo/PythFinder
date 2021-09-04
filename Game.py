import pygame
from pygame.locals import *
import sys
from enum import Enum, auto
from Grid import Grid
from Barrier import Barrier
from Color import Color



class GameState(Enum):
		# Can set game to auto or manual
		# Can set barriers, start point, and end point
		SETUP = auto()
		
		# Can set game to auto or setup
		# Can hit restart
		# Steps through process with button press
		MANUAL = auto()

		# Can set game to manual or setup
		# Can hit restart
		# Steps through process on its own
		AUTO = auto()

class Game:

	def __init__(self, windowWidth, windowHeight):
		pygame.init()

		self.window = pygame.display.set_mode((windowWidth, windowHeight))
		self.window.fill(Color.WHITE)

		self.grid = Grid(0, 0, windowWidth, windowHeight, 20, 20)

		pygame.display.flip()

		self.state = GameState.SETUP


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
			elif event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()
					

	def draw(self):
		self.grid.draw(self.window)