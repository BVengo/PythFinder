from pygame.constants import OPENGL
import math


class Node:
  def __init__(self, cell, gCost, hCost, fCost):
    self.cell = cell
    self.gCost = gCost
    self.hCost = hCost
    self.fCost = fCost

  def set_parent(self, parent):
    self.parent = parent


class AStarAlgorithm:
  def __init__(self, grid, startCell, endCell):
    self.grid = grid
    self.startCell = startCell
    self.endCell = endCell

  def find_path(self):
    openList = []
    closedList = []

    hCost = math.dist((self.startCell.x, self.startCell.y), (self.endCell.x, self.endCell.y))

    startNode = Node(self.startCell, 0, hCost, hCost)
    startNode.set_parent(None)

    openList.append(startNode)

    while len(openList) > 0:
      # Get the node with the lowest fCost
      current = openList[0]

      for node in openList:
        if node.fCost < current.fCost:
          current = node
  
      openList.remove(current)
      closedList.append(current)

    # Target has been reached
      if current.cell == self.endCell:
        return current
      
      neighbours = self.grid.get_neighbours(current.cell)

      for neighbour in neighbours:
        # Ignore cells that the path can't travel through
        if not neighbour.traversable:
          continue
        
        available = True

        for closedNode in closedList:
          if(neighbour == closedNode.cell):
            available = False
            break

        if not available:
          continue

        neighbourNode = None

        for openNode in openList:
          if(neighbour == openNode.cell):
            neighbourNode = openNode
            break
        
        # Set new costs for all neighbours if paths are shorter
        newDist = current.gCost + math.dist((current.cell.x, current.cell.y), (neighbour.x, neighbour.y))

        if neighbourNode == None or newDist < neighbourNode.gCost:
          newGCost = newDist
          newHCost = math.dist((neighbour.x, neighbour.y), (self.endCell.x, self.endCell.y))
          newFCost = newGCost + newHCost

          if neighbourNode == None:
            neighbourNode = Node(neighbour, newGCost, newHCost, newFCost)
            openList.append(neighbourNode)
          else:
            neighbourNode.gCost = newGCost
            neighbourNode.hCost = newHCost
            neighbourNode.fCost = newFCost

          neighbourNode.set_parent(current)
    
    return None