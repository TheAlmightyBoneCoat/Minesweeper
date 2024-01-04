import pygame
from gameConsts import *
from winLose import *

#A general button class
class Button(pygame.sprite.Sprite):
  message = ""
  color = blue
  textColor = black
  fontName = "Calibiri"
  fontSize = 30
  font = ""
  text = ""
  width = ""
  height = ""

  def __init__(self, x, y, width, height):
    super().__init__()
    self.image = pygame.Surface([width, height])
    self.image.fill(blue)
    self.width = width
    self.height = height
    self.rect = self.image.get_rect()
    self.rect.x = x
    self.rect.y = y
    self.message = ""
    self.font = "Calibiri"
    self.fontColor = [0, 0, 0]
    self.fontSize = 10
    self.isButton = True

    self.textX = x
    self.textY = y

  #Regenerates text object
  def regenText(self):
    self.font = pygame.font.SysFont(self.fontName, self.fontSize, True, False)
    self.text = self.font.render(self.message, True, self.fontColor)
    self.textX = self.rect.x + (self.width / 2) - (len(self.message) * 
        self.fontSize / 5)
    self.textY = self.rect.y + (self.height / 10)

  #Sets font and regenerates text
  def setFontName(self, fontName):
    self.font = fontName
    self.regenText()

  #Sets message and regenerates text
  def setMessage(self, newMessage):
    self.message = newMessage
    self.regenText()

  #Sets font size and regenerates text
  def setFontSize(self, fontSize):
    self.fontSize = fontSize
    self.regenText()

  #Sets text color and regenerates text
  def setFontColor(self, fontColor):
    self.fontColor = fontColor
    self.regenText()

  #Sets button color
  def setColor(self, color):
    self.color = color

  def draw(self, screen):
    screen.blit(self.image, self.rect)
    screen.blit(self.text, [self.textX, self.textY])



#Reset button class
class ResetButton(Button):
  def __init__(self, x, y, width, height):
    super().__init__(x, y, width, height)
    self.setFontName("Calibiri")
    self.setFontSize(int(height * 0.8 // 1))
    self.setFontColor([255, 255, 255])
    self.setMessage("Reset")

  #Resets the game
  def onLeftClick(self):
    global currentGameState
    global FIRST_CLICK_HAPPENED
    global TILES_REVEALED
    global INPUT_MODE

    resetBoard()
    placeMines()
    currentGameState = GAME_IN_PROGRESS
    FIRST_CLICK_HAPPENED = False
    TILES_REVEALED = 0

    # if I don't do this, the highlighter disappears
    INPUT_MODE = MOUSE_INPUT

  #Does nothing; purely to fit in spritesGroup()
  def onRightClick(self):
    pass
