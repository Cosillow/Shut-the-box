import pygame
from Box import Box
from Button import Button
from Die import Die

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

    def new_game(self):
        self.hasRolled = False
        self.die.reset()

    def checkClicked(self, position):
        if self.nextRoundBtn.checkClicked(position) and self.box.validTurn(self.die.getRoll()):
            # initialize next turn
            self.hasRolled = False
            self.die.reset()
            self.box.lockBox()

        if self.hasRolled:
            return

        if self.rollBtn1.checkClicked(position):
            self.die.roll(1)
            self.hasRolled = True
        if self.rollBtn2.checkClicked(position):
            self.die.roll(2)
            self.hasRolled = True
            
    def draw(self, screen):
        if self.hasRolled:
            self.nextRoundBtn.draw(screen)
            self.die.draw(screen)
        else:
            self.rollBtn1.draw(screen)
            self.rollBtn2.draw(screen)
