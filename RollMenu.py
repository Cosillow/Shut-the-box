import pygame
from Button import Button
from Die import Die

class RollMenu:
    font = pygame.font.Font('Poppins-Regular.ttf', 50)
    textColor = (0, 0, 0)
    
    def __init__(self, screen_width, screen_height, bx):
        self.x = screen_width/2
        self.y = screen_height-200
        self.rollBtn = Button(self.x, self.y, "roll:", 15, (20,80,60), (0,0,0))
        self.hasRolled = False
        from Box import Box
        self.box: Box = bx # dependency injection
        self.die = Die(self.x, self.y, self.box.get_num_die_needed())
        self.increaseDieBtn = Button(self.x, self.rollBtn.rect.top-self.rollBtn.rect.height, "^", 5, (20,80,60), (0,0,0), self.die.adjust_curr_die, 1)
        self.decreaseDieBtn = Button(self.x, self.rollBtn.rect.top+self.rollBtn.rect.height + 10, "v", 5, (20,80,60), (0,0,0), self.die.adjust_curr_die, -1)

    def update(self):
        if self.box.validTurn(self.die.getRoll()):
            self.hasRolled = False
            self.die.reset()
            self.box.lockBox()

    def new_game(self):
        self.hasRolled = False
        self.die.reset()

    def checkClicked(self, position):
        if self.hasRolled:
            # player is thinking or finishing their turn
            return
            
        # player is about to roll
        if self.increaseDieBtn.checkClicked(position):
            pass
        elif self.decreaseDieBtn.checkClicked(position):
            pass
        elif self.rollBtn.checkClicked(position):
            # elif prevents multiple occurances if button overlap
            self.die.roll()
            self.hasRolled = True
            self.box.checkLoss(self.die.getRoll())
            
    def draw(self, screen):
        if self.hasRolled:
            self.die.draw(screen)
        else:
            self.rollBtn.draw(screen)
            self.increaseDieBtn.draw(screen)
            self.decreaseDieBtn.draw(screen)
            renderedText = RollMenu.font.render(str(self.die.currDie), True, RollMenu.textColor)
            screen.blit(renderedText, (self.x + self.rollBtn.rect.width, self.y))
