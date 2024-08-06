from enum import Enum
import pygame
from Box import Box
from Button import Button
from Die import Die

class gameState(Enum):
    playing = 0
    lost = 1
    won = 2

class RollMenu:
    font = pygame.font.Font('Poppins-Regular.ttf', 50)
    textColor = (0, 0, 0)
    
    def __init__(self, screen_width, screen_height):
        self.die = Die(screen_width - (screen_width/4), screen_height-200)
        self.rollBtn1 = Button(screen_width/4, screen_height-200, "Roll 1", 15, (20,80,60), (0,0,0))
        self.rollBtn2 = Button(screen_width/2, screen_height-200, "Roll 2", 15, (20,80,60), (0,0,0))
        self.nextRoundBtn = Button(screen_width/3, screen_height-200, "Next", 15, (20,80,60), (0,0,0))
        self.hasRolled = False
        self.box = Box() # access existing panels
        self.gameState = gameState.playing
        self.screen_width = screen_width
        self.screen_height = screen_height

    def checkClicked(self, position):
        if not self.gameState.playing:
            return

        if self.nextRoundBtn.checkClicked(position):
            if self.box.checkWin():
                self.gameState = gameState.won
            if self.box.validTurn(self.die.getRoll()):
                # initialize next turn
                self.hasRolled = False
                self.box.lockBox()

        if self.hasRolled:
            return

        if self.rollBtn1.checkClicked(position):
            self.hasRolled = True
            if self.box.checkLoss(self.die.roll(1)):
                self.gameState = gameState.lost
        if self.rollBtn2.checkClicked(position):
            self.hasRolled = True
            if self.box.checkLoss(self.die.roll(2)):
                self.gameState = gameState.lost
            
    def update(self, screen):
        if self.hasRolled:
            self.nextRoundBtn.update(screen)
            self.die.update(screen)
        else:
            self.rollBtn1.update(screen)
            self.rollBtn2.update(screen)