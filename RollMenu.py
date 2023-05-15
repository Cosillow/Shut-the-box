from enum import Enum
import pygame
from box import Box
from button import Button
from die import Die


class gameState(Enum):
    running = 0
    lost = 1
    won = 2
    

class RollMenu:
    font = pygame.font.Font('Poppins-Regular.ttf', 50)
    textColor = (0, 0, 0)
    
    def __init__(self, screen, screen_width, screen_height):
        self.die = Die(screen_width - (screen_width/4), screen_height-200, screen)
        self.rollBtn1 = Button(screen_width/4, screen_height-200, "Roll 1", 15, screen, (20,80,60), (0,0,0))
        self.rollBtn2 = Button(screen_width/2, screen_height-200, "Roll 2", 15, screen, (20,80,60), (0,0,0))
        self.nextRoundBtn = Button(screen_width/3, screen_height-200, "Next", 15, screen, (20,80,60), (0,0,0))
        self.hasRolled = False
        self.box = Box()
        self.gameState = gameState.running
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.screen = screen

    def checkClicked(self, position):
        if self.rollBtn1.checkClicked(position) and not self.hasRolled:
            self.hasRolled = True
            if self.box.checkLoss(self.die.roll(1)):
                self.gameState = gameState.lost
        if self.rollBtn2.checkClicked(position) and not self.hasRolled:
            self.hasRolled = True
            if self.box.checkLoss(self.die.roll(2)):
                self.gameState = gameState.lost
        if self.nextRoundBtn.checkClicked(position):
            if self.box.checkWin():
                self.gameState = gameState.won
            if self.box.validTurn(self.die.getRoll()):
                # initialize next turn
                self.hasRolled = False
                self.box.lockBox()
            
    def update(self):
        if self.gameState is gameState.won or self.gameState is gameState.lost:
            txtString = 'You win' if self.gameState is gameState.won else 'You lose'
            winText = RollMenu.font.render(txtString, True, RollMenu.textColor)
            width1 = winText.get_rect().width
            self.screen.blit(winText, (self.screen_width / 2 - width1 / 2, self.screen_height / 2))
        elif not self.hasRolled:
            self.rollBtn1.update()
            self.rollBtn2.update()
        else:
            self.nextRoundBtn.update()
            self.die.update()