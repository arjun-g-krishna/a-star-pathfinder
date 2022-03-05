# imports

import pygame
import math
from queue import PriorityQueue

# Initialize the display and colors

WIDTH = 800
WIN = pygame.display.set_mode((WIDTH,WIDTH))
pygame.display.set_caption("A* path-finding algorithm")
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 255, 0)
YELLOW = (255, 255, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
PURPLE = (128, 0, 128)
ORANGE = (255, 165 ,0)
GREY = (128, 128, 128)
TURQUOISE = (64, 224, 208)

# Class to define the nodes ie. a spot. Keeps track of row-column positions, colors and its neighbors

class  Spot(object):

	def __init__(self, row,col,width,total_rows):
		self.row = row
		self.col = col
		self.x = row*width
		self.y = col*width
		self.color = WHITE
		self.neighbors = []
		self.width = width
		self.total_rows = total_rows
	# function to get the position	
	
	def  get_pos(self):
		return self.row,self.col
	
	# functions to check the state of the nodes

	def is_closed(self):
		return self.color==RED
	def is_open(self):
		return self.color==GREEN
	def is_barrier(self):
		return  self.color==BLACK
	def is_start(self):
		return self.color==ORANGE
	def is_end(self):
		return self.color==TURQUOISE
	def reset(self):
		self.color = WHITE
	
	# functions to set the state of the nodes
	
	def make_closed(self):
		self.color = RED
	def make_open(self):
		self.color = GREEN
	def make_barrier(self):
		self.color = BLACK
	def make_start(self):
		self.color = ORANGE
	def make_end(self):
		self.color = TURQUOISE
	def make_path(self):
		self.color = PURPLE

	# Draw method draws the window on the screen

	def draw(self,win):
		pygame.draw.rect(win,self.color,self.x,self.y,self.width,self.width)
	def update_neighbors(self,grid):
		pass
	def __lt__(self):
		return False

# The h function

def h(p1,p2):
	x1,y1 = p1
	x2,y2 = p2
	return abs(x1-x2) + abs(y1-y2)

# function to make the grid

def make_grid:
	grid = []
	gap = width // rows
	for i in range(rows):
		grid.append([])
		for j in range(rows):
			spot = new Spot(i,j,gap,rows)
			grid[i].append(spot)
	return grid

# functions to draw the grid and grid lines

def draw_grid(win,rows,width):
	gap = width // rows
	for i in range(rows):
		pygame.draw.line(win,GREY,(0,i*gap),(width,i*gap))
		for j in range(rows):
			pygame.draw.line(win,GREY,(j*gap,0),(j*gap,width))

def draw(win,grid,rows,width):
	win.fill(WHITE)
	for row in grid:
		for spot in row:
			spot.draw(win)
	draw_grid(win,rows,width)
	pygame.display.update()

# function that takes the mouse position and determines what node to update

def get_clicked_position(pos,rows,width):
	gap = width // rows
	y,x = pos
	row = y // gap
	col = x // gap
	return row,col

# Main function

def main(win,width):
		