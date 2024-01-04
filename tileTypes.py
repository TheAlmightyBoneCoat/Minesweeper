import pygame
from gameConsts import *
from initGlobals import *
from loadImages import *
from winLose import *
from keybind import keybinds
#from minesweeper import *

#Clickable tile class
class Tile(pygame.sprite.Sprite):
    #Init array and sprite data
    def __init__(self, x, y):
        super().__init__()
        self.image = hiddenTile
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        #Calculate for size of each tile, width of screen border, space between
        #tiles.....
        self.rect.x = x * (TILE_WIDTH + BUTTON_BETWEEN_WIDTH) + MARGIN_WIDTH
        self.rect.y = y * (TILE_HEIGHT + BUTTON_BETWEEN_HEIGHT) + MARGIN_HEIGHT

        self.value = VAL_BLANK
        self.hidden = True
        self.flagged = False
        
    #Sets this tile to a mine.
    #Return: true if tile was successfully set; false if it was already a mine
    def setMine(self):
      if self.value != VAL_MINE:
        self.value = VAL_MINE
        return True
      else:
        return False
        
    #Calculates the number of mines surrounding this tile.
    #If the function returns VAL_MINE, this tile is a mine.
    def getValue(self, grid):
      #Am I a mine?
      if (self.value == VAL_MINE):
        return VAL_MINE
      
      #Has my value been calculated already?
      if (self.value != VAL_BLANK):
        return self.value
      
      #Otherwise, let's check if any of my neighbors are mines
      #It's OK to check ourselves, since we've established we're not a mine
      self.value = 0
      for i in range(self.y - 1, self.y + 2):
        for j in range(self.x - 1, self.x + 2):
          #If the value is in valid range
          if (i >= 0 and i < NUM_ROWS and j >= 0 and j < NUM_COLUMNS):
            #Check if it's a mine
            if (grid[i][j].value == VAL_MINE):
              self.value += 1
      
      #Return the sum
      return self.value


    #Undo all user modification of this tile
    def reset(self):
      self.image = hiddenTile
      self.value = VAL_BLANK
      self.hidden = True
      self.flagged = False



    #Reveals this tile.
    #If it's blank, other tiles around it are also revealed.
    #If it's a mine, the game ends.
    def reveal(self, grid):
      #Am I already revealed
      if not self.hidden:
        return
      
      else:
        self.hidden = False
        global drawFrame
        
        #If I'm a mine
        if self.value == VAL_MINE:
          #Make sure this isn't a protected tile
          if (not FIRST_CLICK_PROTECTED) or FIRST_CLICK_HAPPENED:
            lose()
            return
          
          else:
            self.value = VAL_BLANK
            print("Mine removed from protected tile!")
            
        #If there are no surrounding mines
        if self.getValue(grid) == 0:
          #Reveal all surrounding tiles
          #Be careful not to call reveal on yourself again
          for i in range(self.y - 1, self.y + 2):
            if i >= 0 and i < NUM_ROWS:
              for j in range(self.x - 1, self.x + 2):
                #If this is a valid value
                 if j >= 0 and j < NUM_COLUMNS:
                  #If we're not checking ourself
                  if i != self.y or j != self.x:
                    grid[i][j].reveal(grid)
                    
        self.image = tileImagesArray[self.getValue(grid)]
        drawFrame = True

        global TILES_REVEALED
        TILES_REVEALED += 1


    #Sets flagged to true and changes image accordingly
    def flag(self):
      #Can't flag revealed tile
      if self.hidden:
        self.flagged = True
        self.image = flagTile
        global drawFrame
        drawFrame = True

    #Sets flagged to false and changes image accordingly
    def unflag(self):
      self.flagged = False
      self.image = hiddenTile
      global drawFrame
      drawFrame = True

    # Counts flags surrounding this tile
    def flagsSurrounding(self, grid):
        flagCount = 0
        for i in range(self.y - 1, self.y + 2):
            if i >= 0 and i < NUM_ROWS:
                for j in range(self.x - 1, self.x + 2):
                    if j >= 0 and j < NUM_COLUMNS:
                        # Assume this function will never be called
                        # on a flagged tile
                        if grid[i][j].flagged:
                            flagCount += 1
        return flagCount

               
    def chord(self, grid):
        flagCount = self.flagsSurrounding(grid)
        if flagCount == self.getValue(grid):
            for i in range(self.y - 1, self.y + 2):
                if i >= 0 and i < NUM_ROWS:
                    for j in range(self.x - 1, self.x + 2):
                        if j >= 0 and j < NUM_COLUMNS:
                            if (grid[i][j].hidden and not grid[i][j].flagged):
                                grid[i][j].reveal(grid)

        else:
            pass # TODO: hidden tiles flash red
 
    #Action to take when left-clicked
    #Reveal myself, and record that the first click happened
    def onLeftClick(self):
      global FIRST_CLICK_HAPPENED
      if currentGameState == GAME_IN_PROGRESS:
        #print(currentGameState)
        if not self.flagged:
            if not self.hidden:
                self.chord(grid)
            else:
                self.reveal(grid)
        FIRST_CLICK_HAPPENED = True

    #Action to take when right-clicked
    #Toggle flagged status
    def onRightClick(self):
      #Don't respond to input if game is over, and don't flag if we're revealed
      if currentGameState == GAME_IN_PROGRESS:
        #Toggle flagged status
        if self.flagged == True:
          self.unflag()
        else:
          self.flag()



#Object for the tile selector
class tileHighlighter(pygame.sprite.Sprite):

  def __init__(self):

    self.x = 0
    self.y = 0
    self.hidden = True
    super().__init__()
    self.image = invisible
    self.rect = self.image.get_rect()
    self.rect.x = MARGIN_WIDTH + (self.x * (TILE_WIDTH + BUTTON_BETWEEN_WIDTH))
    self.rect.y = MARGIN_HEIGHT + (self.y * (TILE_HEIGHT + BUTTON_BETWEEN_HEIGHT))

  #Adds the given x and y to this tile's coordinates.
  #Note these are grid coordinates, not screen coordinates.
  #x - How much to add to the x-position.
  #y - How much to add to the y-position.
  def addPos(self, x, y):
    #print("Highlighter went from x = " + str(self.x), end=" ")
    self.x += x
    
    #Did we go out of bounds?
    if (self.x < 0):
      self.x = NUM_COLUMNS - 1
    elif self.x >= NUM_COLUMNS:
      self.x = 0
      
    self.rect.x = MARGIN_WIDTH + self.x * (TILE_WIDTH + BUTTON_BETWEEN_WIDTH)
    #print("to x = " + str(self.x), end = ", ")

    #print("y = " + str(self.y), end=" ")
    self.y += y
    
    # Do another out-of-bounds check
    if (self.y < 0):
      self.y = NUM_ROWS - 1
    elif self.y >= NUM_ROWS:
      self.y = 0
      
    self.rect.y = MARGIN_HEIGHT + self.y * (TILE_HEIGHT + BUTTON_BETWEEN_HEIGHT)
    #print("to y = " + str(self.y))

    global drawFrame
    drawFrame = True

  #Some addPos calls for readability
  def moveRight(self):
    self.addPos(1, 0)

  def moveLeft(self):
    self.addPos(-1, 0)

  def moveUp(self):
    self.addPos(0, -1)

  def moveDown(self):
    self.addPos(0, 1)

  #Process user input
  #TODO: Adapt to reset button
  def move(self, key):
    if currentGameState != GAME_IN_PROGRESS:
        self.despawn()
        return

    global INPUT_MODE
    
    # Are we just getting into key mode?
    if INPUT_MODE == MOUSE_INPUT:
      INPUT_MODE = KEY_INPUT
      self.spawn()
      return
    
    # Movement
    if (key == keybinds.keyFromAction(keybinds.GO_LEFT)):
      self.moveLeft()
    elif (key == keybinds.keyFromAction(keybinds.GO_RIGHT)):
      self.moveRight()
    elif (key == keybinds.keyFromAction(keybinds.GO_UP)):
      self.moveUp()
    elif (key == keybinds.keyFromAction(keybinds.GO_DOWN)):
      self.moveDown()


  #Reveal ourselves in key mode
  def spawn(self):
    print("Spawning...")
    self.image = tileSelected
    self.x = 0
    self.y = 0
    self.rect = self.image.get_rect()
    self.rect.x = MARGIN_WIDTH + self.x * (TILE_WIDTH + BUTTON_BETWEEN_WIDTH)
    self.rect.y = MARGIN_HEIGHT + self.y * (TILE_HEIGHT + BUTTON_BETWEEN_HEIGHT)
    global drawFrame
    drawFrame = True

  #Hide ourselves in mouse mode
  def despawn(self):
    global INPUT_MODE
    INPUT_MODE = MOUSE_INPUT

    self.image = invisible
    global drawFrame
    drawFrame = True

  #Compatibility functions - essentially useless
  def onLeftClick(self):
    pass

  def onRightClick(self):
    pass
