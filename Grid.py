from Cell import Cell
from Barrier import Barrier
from StartCell import StartCell
from EndCell import EndCell
from Color import Color


class Grid:

	fill = Color.WHITE
	border = Color.BLACK

	placedStart = False
	placedEnd = False

	def __init__(self, x, y, width, height, cols, rows):
		self.x = x
		self.y = y

		self.width = width
		self.height = height

		self.cols = cols
		self.rows = rows

		self.cellWidth = int(self.width / self.cols)
		self.cellHeight = int(self.height / self.rows)

		self.populate()


	def populate(self):

		self.cells = []

		for col in range(0, self.cols):

			col_vals = []

			for row in range(0, self.rows):
				
				cellX = self.x + int(self.cellWidth * col)
				cellY = self.y + int(self.cellHeight * row)

				col_vals.append(Cell(cellX, cellY, self.cellWidth, self.cellHeight, self.fill, self.border))
			
			self.cells.append(col_vals)

	def clear(self):
		self.populate()
		self.placedStart = False
		self.placedEnd = False


	def draw(self, window):

		for col in range(0, self.cols):
			for row in range(0, self.rows):
				self.cells[col][row].draw(window)


	def getGridPos(self, pos):
		col = int((pos[0] - self.x) / self.cellWidth)
		row = int((pos[1] - self.y) / self.cellHeight)

		return (col, row)


	def getCellPosFromPoint(self, pos):
		gridPos = self.getGridPos(pos)

		return self.getCellPosFromGrid(gridPos)


	def getCellPosFromGrid(self, gridPos):
		cellX = self.x + int(self.cellWidth * gridPos[0])
		cellY = self.y + int(self.cellHeight * gridPos[1])

		return (cellX, cellY)


	def contains(self, pos):
		return (pos[0] >= self.x and pos[0] < (self.x + self.width) and 
				pos[1] >= self.y and pos[1] < (self.y + self.height))
	

	def handle_lclick(self, pos):
		if not self.contains(pos):
			return

		gridPos = self.getGridPos(pos)
		cellPos = self.getCellPosFromGrid(gridPos)

		currentCellType = type(self.cells[gridPos[0]][gridPos[1]])
		
		if currentCellType != Barrier:
			self.cells[gridPos[0]][gridPos[1]] = Barrier(cellPos[0], cellPos[1], self.cellWidth, self.cellHeight)

			if currentCellType == StartCell:
				if self.placedEnd:
					endCellPos = self.getCellPosFromGrid(self.endPos)

					self.cells[self.endPos[0]][self.endPos[1]] = Cell(endCellPos[0], endCellPos[1], self.cellWidth, self.cellHeight, self.fill, self.border)
					self.placedEnd = False
				
				self.cells[gridPos[0]][gridPos[1]] = Barrier(cellPos[0], cellPos[1], self.cellWidth, self.cellHeight)
				self.placedStart = False

			if currentCellType == EndCell:
				self.cells[gridPos[0]][gridPos[1]] = Barrier(cellPos[0], cellPos[1], self.cellWidth, self.cellHeight)
				self.placedEnd = False
		else:
			self.cells[gridPos[0]][gridPos[1]] = Cell(cellPos[0], cellPos[1], self.cellWidth, self.cellHeight, self.fill, self.border)


	def handle_rclick(self, pos):
		if not self.contains(pos):
			return
		
		gridPos = self.getGridPos(pos)
		cellPos = self.getCellPosFromGrid(gridPos)

		currentCellType = type(self.cells[gridPos[0]][gridPos[1]])

		if currentCellType != StartCell and currentCellType != EndCell:
			if self.placedEnd:
				pass
			elif self.placedStart:
				self.cells[gridPos[0]][gridPos[1]] = EndCell(cellPos[0], cellPos[1], self.cellWidth, self.cellHeight)
				self.endPos = gridPos
				self.placedEnd = True
			else:
				self.cells[gridPos[0]][gridPos[1]] = StartCell(cellPos[0], cellPos[1], self.cellWidth, self.cellHeight)
				self.startPos = gridPos
				self.placedStart = True
		elif currentCellType == StartCell:
			if self.placedEnd:
				endCellPos = self.getCellPosFromGrid(self.endPos)

				self.cells[self.endPos[0]][self.endPos[1]] = Cell(endCellPos[0], endCellPos[1], self.cellWidth, self.cellHeight, self.fill, self.border)
				self.placedEnd = False
			
			self.cells[gridPos[0]][gridPos[1]] = Cell(cellPos[0], cellPos[1], self.cellWidth, self.cellHeight, self.fill, self.border)
			self.placedStart = False
		elif currentCellType == EndCell:
			self.cells[gridPos[0]][gridPos[1]] = Cell(cellPos[0], cellPos[1], self.cellWidth, self.cellHeight, self.fill, self.border)
			self.placedEnd = False