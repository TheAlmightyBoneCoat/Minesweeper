import pygame

#Define some colors...
black = [0,0,0]
white = [255,255,255]
red = [255,0,0]
green = [0,255,0]
blue = [0,0,255]

#Define some constants
TILE_WIDTH = 20
TILE_HEIGHT = 26
BUTTON_BETWEEN_WIDTH = 2 #How much space in between the buttons
BUTTON_BETWEEN_HEIGHT = BUTTON_BETWEEN_WIDTH
NUM_ROWS = 16    #How many rows of tiles?
NUM_COLUMNS = 30 #How many columns of tiles?
NUM_MINES = 99   #How many mines are on the board?

GRID_WIDTH = (NUM_COLUMNS * TILE_WIDTH) + (
    (NUM_COLUMNS - 1) * BUTTON_BETWEEN_WIDTH)
GRID_HEIGHT = (NUM_ROWS * TILE_HEIGHT) + (
    (NUM_ROWS - 1) * BUTTON_BETWEEN_HEIGHT)

screenSize = [1000, 700] 
MARGIN_WIDTH = (screenSize[0] - GRID_WIDTH) / 2
MARGIN_HEIGHT = (screenSize[1] - GRID_HEIGHT) / 2

#Clamp maximum number of mines to number of tiles, minus corners
if NUM_MINES > (NUM_ROWS * NUM_COLUMNS) - 16:
  NUM_MINES = NUM_ROWS * NUM_COLUMNS - 16
VAL_MINE = -1 #Special value to indicate this tile is a mine
VAL_BLANK = 9 #Shows this tile's value needs to be calculated

#Mouse button values
LEFT_CLICK = 1
RIGHT_CLICK = 3

#Option so that the first click is never on a mine
FIRST_CLICK_PROTECTED = True
FIRST_CLICK_HAPPENED = False

#Input mode definitions
MOUSE_INPUT = 0
KEY_INPUT = 1

#Game state variables
GAME_IN_PROGRESS = 0
GAME_WIN = 1
GAME_LOSE = 2

