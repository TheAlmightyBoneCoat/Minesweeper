import pygame
from gameConsts import *

#Keep track of progress toward win condition
TILES_REVEALED = 0

INPUT_MODE = MOUSE_INPUT

#Set up the window
screen = pygame.display.set_mode(screenSize)
pygame.display.set_caption("Minesweeper")


#Sets to true when we want to exit the main loop
done = False
currentGameState = GAME_IN_PROGRESS

drawFrame = True
grid = []
