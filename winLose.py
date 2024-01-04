# This module needs a better name
# Not only does it store the win and lose functions,
# but also general stuff related to revealing/resetting the board

import random

from gameConsts import *
from loadImages import *
from initGlobals import *

def revealBoard():
  global grid
  for i in range(NUM_ROWS):
    for j in range(NUM_COLUMNS):
      #Was it flagged?
      
      if grid[i][j].flagged == True:
        #Change it if it was flagged incorrectly
        if grid[i][j].getValue(grid) != VAL_MINE:
          grid[i][j].image = incorrectFlag
          
      #Otherwise, reveal if it's a mine
      else:
        if grid[i][j].getValue(grid) == VAL_MINE:
          grid[i][j].image = mineTile

#Reveals all mines and incorrect flags
def lose():
  global currentGameState
  currentGameState = GAME_LOSE
  revealBoard()

#Flags all remaining mines
def win():
  global currentGameState
  currentGameState = GAME_WIN
  revealBoard()

#Wipe the board clean
def resetBoard():
  for i in range(NUM_ROWS):
    for j in range(NUM_COLUMNS):
      grid[i][j].reset()

#Place the mines
def placeMines():
  global grid

  minesPlaced = 0 #How many mines we've placed so far
  while minesPlaced < NUM_MINES:
    #Generate a random location for the mine
    randRow = random.randrange(0, NUM_ROWS)
    randCol = random.randrange(0, NUM_COLUMNS)
    #Leave some space in the corners
    if randRow < 2 or randRow > NUM_ROWS - 2:
      if randCol < 2 or randCol > NUM_COLUMNS - 2:
        continue
    #Make that tile a mine, if it isn't already
    if grid[randRow][randCol].value != VAL_MINE:
      grid[randRow][randCol].value = VAL_MINE
      minesPlaced += 1
