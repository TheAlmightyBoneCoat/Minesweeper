# -*- coding: utf-8 -*-
"""
Created on Thu Dec 20 14:34:25 2018

@author: Thomas Powell

A Minesweeper game that I created after boarding a six-hour flight
and discovering my computer did not have it installed.
"""

#Get our Pygame stuff initialized
import pygame
pygame.init()
import random #To randomly place mines
from initGlobals import *
from gameConsts import *
#from tileTypes import *
import tileTypes
from buttonTypes import *
from loadImages import *
from keybind import keybinds

#Our array of tiles
highlightGroup = pygame.sprite.Group()
#ALL sprites in this group MUST have both onLeftClick and onRightClick defined
spritesGroup = pygame.sprite.Group()
buttonsGroup = pygame.sprite.Group()

highlightTile = tileTypes.tileHighlighter()

#Sets tile width and height parameters to the size of a loaded image
#By default, it's set according to hiddenTile.
def setTileDims(image = hiddenTile):
  global TILE_WIDTH
  global TILE_HEIGHT
  dimsRect = image.get_rect()
  TILE_WIDTH = dimsRect.x
  print(TILE_WIDTH, end=" ")
  TILE_HEIGHT = dimsRect.y
  print(TILE_HEIGHT)


          




#Centers the grid in the middle of the screen
def calcMargins():
  global MARGIN_WIDTH
  global MARGIN_HEIGHT
  #First, the horizontal margin
  MARGIN_WIDTH = (screenSize[0] - ((TILE_WIDTH + BUTTON_BETWEEN_WIDTH) * NUM_COLUMNS)) / 2
  MARGIN_HEIGHT = (screenSize[1] - ((TILE_HEIGHT + BUTTON_BETWEEN_HEIGHT) * NUM_ROWS)) / 2


#Populate the grid
for i in range(NUM_ROWS):
  grid.append([])
  for j in range(NUM_COLUMNS):
    newTile = tileTypes.Tile(j, i)
    grid[i].append(newTile)
    spritesGroup.add(newTile)


#Creates a text display connected to a certain button and adds it to the text list.
#Inputs:
#button: A Button object we'll center ourselves on.
#message: What the text will say.
#color: The text color.
def addButtonText(button, message, color=black):
  #Make sure to truncate font size to int
  fontSize = int(button.height * 0.8 // 1)
  newFont = pygame.font.SysFont("Calibiri", fontSize, True, False)
  newText = newFont.render(message, True, color)
  texts.append(newText)
  textCoords.append([button.rect.x + (button.width / 2) - (len(message) * fontSize / 5),
      button.rect.y + (button.height / 10)])




def updateScreen():
    global drawFrame
    if drawFrame:
       # print("Drawing frame")
        screen.fill(white)
        spritesGroup.draw(screen)
        for button in buttonsGroup:
            button.draw(screen)
        #Ensure highlighter is drawn on top of everything
        highlightGroup.draw(screen)
        #Draw all text
    #    for i in range(len(texts)):
     #     screen.blit(texts[i], textCoords[i])

        pygame.display.flip()
        #drawFrame = False
        drawFrame = True

#Center our grid
calcMargins()

#Add UI buttons
resetButton = ResetButton(screenSize[0] * 2/5, MARGIN_HEIGHT / 4, screenSize[0] / 5,
                          MARGIN_HEIGHT / 2)
buttonsGroup.add(resetButton)
#spritesGroup.add(highlightTile)
texts = [] #Array of text objects
textCoords = [] # Coordinates of the text - 
                # texts[0] gets drawn at textCoords[0], etc.

#Add UI text
addButtonText(resetButton, "Reset", white)

#Give the highlight tile its own group
highlightGroup.add(highlightTile)
placeMines()
      
#Main loop
while not done:
  #if drawFrame:
   #   print("drawFrame")
  #Process mouse input
  for event in pygame.event.get():
      if event.type == pygame.QUIT:
          done = True
      elif event.type == pygame.MOUSEBUTTONDOWN:
          #INPUT_MODE = MOUSE_INPUT
          highlightTile.despawn()
          [mouseX, mouseY] = pygame.mouse.get_pos()
          #Test collision
          for sprite in spritesGroup:
            if sprite.rect.collidepoint(mouseX, mouseY):
              #What type of click was it?
              if event.button == LEFT_CLICK:
                sprite.onLeftClick()
              elif event.button == RIGHT_CLICK:
                sprite.onRightClick()
          for button in buttonsGroup:
            if button.rect.collidepoint(mouseX, mouseY):
              #What type of click was it?
              if event.button == LEFT_CLICK:
                button.onLeftClick()
      #Switch to keyboard mode
      elif event.type == pygame.KEYDOWN:
        if event.key == keybinds.keyFromAction(keybinds.REVEAL_TILE):
            grid[highlightTile.y][highlightTile.x].onLeftClick()
        elif event.key == keybinds.keyFromAction(keybinds.FLAG_TILE):
            grid[highlightTile.y][highlightTile.x].onRightClick()
        else:
            highlightTile.move(event.key)

  #Have we won yet?
  if TILES_REVEALED == (NUM_ROWS * NUM_COLUMNS) - NUM_MINES:
    win()

  #Draw the grid
  updateScreen()
pygame.quit()

