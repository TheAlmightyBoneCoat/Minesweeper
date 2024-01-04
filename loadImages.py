import pygame
from gameConsts import *

#Load images
hiddenTile = pygame.image.load("minesweeper_data/hiddenTile.png").convert()
blankTile = pygame.image.load("minesweeper_data/blankTile.png").convert()
flagTile = pygame.image.load("minesweeper_data/flaggedTile.png").convert()
incorrectFlag = pygame.image.load("minesweeper_data/incorrectFlag.png").convert()
mineTile = pygame.image.load("minesweeper_data/mine.png").convert()
oneTile = pygame.image.load("minesweeper_data/oneTile.png").convert()
twoTile = pygame.image.load("minesweeper_data/twoTile.png").convert()
threeTile = pygame.image.load("minesweeper_data/threeTile.png").convert()
fourTile = pygame.image.load("minesweeper_data/fourTile.png").convert()
fiveTile = pygame.image.load("minesweeper_data/fiveTile.png").convert()
sixTile = pygame.image.load("minesweeper_data/sixTile.png").convert()
sevenTile = pygame.image.load("minesweeper_data/sevenTile.png").convert()
eightTile = pygame.image.load("minesweeper_data/eightTile.png").convert()
tileSelected = pygame.image.load("minesweeper_data/tileSelected.png").convert()
invisible = pygame.image.load("minesweeper_data/invisible.png").convert()
tileSelected.set_colorkey(white)
invisible.set_colorkey(white)

#Make a convenient array for number of mines = image index
tileImagesArray = [blankTile, oneTile, twoTile, threeTile, fourTile, fiveTile,
    sixTile, sevenTile, eightTile]
