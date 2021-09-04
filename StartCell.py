from Cell import Cell
from Color import Color

class StartCell(Cell):

	fill = Color.BLUE
	border = Color.BLACK

	def __init__(self, x, y, width, height):
		super().__init__(x, y, width, height, self.fill, self.border)
