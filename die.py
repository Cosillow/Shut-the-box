import random, pygame
pygame.font.init()

class Die:
    # Class variables
    font = pygame.font.Font('Poppins-Regular.ttf', 50)
    textColor = (0, 0, 0)

    def __init__(self, x, y, screen):
        self.x = x
        self.y = y
        self.num1 = 0
        self.num2 = 0
        self.screen = screen

    def roll(self, numDie = 2):
        self.num1 = random.randrange(1,7)
        self.num2 = 0
        if numDie == 2:
            self.num2 =random.randrange(1,7)
        return self.getRoll()
    
    def getRoll(self):
        return self.num1 + self.num2

    def update(self):
        roll1 = Die.font.render(str(self.num1), True, Die.textColor)
        roll2 = Die.font.render(str(self.num2), True, Die.textColor)
        width1 = roll1.get_rect().width
        width2 = roll2.get_rect().width
        totalWidth = width1 + width2
        if self.num1:
            self.screen.blit(roll1, (self.x - (totalWidth - width1), self.y))
        if self.num2:
            self.screen.blit(roll2, (self.x + (totalWidth - width2), self.y))
