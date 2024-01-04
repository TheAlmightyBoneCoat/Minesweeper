import pygame
from gameConsts import *
from buttonTypes import *
from keybind import *
 

# We have one button for each settable action
# plus a "return to game" button.
# Each displays the key the action is currently set to
# Two ways to choose and set a keybind:

# 1. Mouse method
#    a. User left-clicks on corresponding button
#    b. Button text changes to "Waiting for input..."
#    c. If the user presses "Back" at this point, the keybind is unchanged
#    d. The user then presses the desired new keybind
#    e. If said key is already in use, it unbinds the other key

# 2. Tab button method
#    a. User presses Tab once. The topmost button is highlighted.
#    b. If the user presses Tab again, the highlight will advance to the next button.
#       i.  If the user tabs through all the buttons, the highlighter will 
#           then go to the "Return to game" button.
#       ii. If the user presses Tab again, the highlighter will go back to
#           the topmost button.
#    c. If the user presses a non-Tab key with a button highlighted,
#       that will be set as the new keybind.
#       i. If that key is already in use, the key currently using it
#          will be unbound.


class ControlsMenu():
    def __init__(self):
        self.rowsToDraw = {} # Key = action, value = label
        self.rowsToDraw[keybinds.REVEAL_TILE] = "Reveal tile"
        self.rowsToDraw[keybinds.FLAG_TILE] = "Flag tile"
        self.rowsToDraw[keybinds.RESET_BOARD] = "New game"
        self.rowsToDraw[keybinds.GO_LEFT] = "Move highlighter left"
        self.rowsToDraw[keybinds.GO_RIGHT] = "Move highlighter right"
        self.rowsToDraw[keybinds.GO_UP] = "Move highlighter up"
        self.rowsToDraw[keybinds.GO_DOWN] = "Move highlighter down"

        self.NUM_ROWS = len(self.rowsToDraw)
        self.HORIZONTAL_MARGIN = 50
        self.VERTICAL_MARGIN = 50
        self.ROW_WIDTH = screenSize[0] - (2 * self.HORIZONTAL_MARGIN)
        # NUM_ROWS + 1 to make room for "go back" button
        self.ROW_HEIGHT = ((screenSize[1] - (2 * self.VERTICAL_MARGIN)) / 
            (self.NUM_ROWS + 1))
        
        i = 0
        for action in rowsToDraw:
            self.drawControlsMenuRow(rowsToDraw[action], action, HORIZONTAL_MARGIN,
                VERTICAL_MARGIN + (ROW_HEIGHT * i), ROW_WIDTH, ROW_HEIGHT)
            i += 1

    # Draw a button in the controls menu with its associated label
    # E.g. Reveal tile:        Left click
    #        ^ label            ^ currently mapped key
    # Label   - Label for the action this will set.
    # Action  - Keybind-changing function for this button
    # x, y    - Screen coordinates for label on left.
    # width, height - Parameters for the "box" of the row
    #                 (including label, button, and margin)
    def drawControlsMenuRow(self, label, action, x, y, width, height):
        pass
