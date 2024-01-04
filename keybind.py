# A singleton class that keeps track of all keybindable actions
import pygame

class KeybindController():
    # Enum of codes for all the different actions
    REVEAL_TILE = 0
    FLAG_TILE = 1
    RESET_BOARD = 2
    GO_LEFT = 3
    GO_RIGHT = 4
    GO_DOWN = 5
    GO_UP = 6

    UNBOUND  = "Unbound"

    def __init__(self):
        self.__keyFromAction = {}
        self.__actionFromKey = {}

        # TODO: Make a keybinds file that this reads from
        self.insertKeybind(pygame.K_a, KeybindController.GO_LEFT)
        self.insertKeybind(pygame.K_w, KeybindController.GO_UP)
        self.insertKeybind(pygame.K_d, KeybindController.GO_RIGHT)
        self.insertKeybind(pygame.K_s, KeybindController.GO_DOWN)
        self.insertKeybind(pygame.K_e, KeybindController.REVEAL_TILE)
        self.insertKeybind(pygame.K_r, KeybindController.FLAG_TILE)
        self.insertKeybind(pygame.K_f, KeybindController.RESET_BOARD)
        
    # Key    - the key you press for this action
    # action - the int code associated with this key
    #          (see the static vars)
    def insertKeybind(self, key, action):
        # Disallow same key bound to multiple actions
        try:
            dummy = self.__actionFromKey[key]
        except KeyError:
            self.__keyFromAction[action] = key
            self.__actionFromKey[key] = action

    def actionFromKey(self, key):
        return self.__actionFromKey[key]

    def keyFromAction(self, action):
        return self.__keyFromAction[action]

keybinds = KeybindController()
