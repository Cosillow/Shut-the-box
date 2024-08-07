import random, pygame

class Die:
    font = pygame.font.Font('Poppins-Regular.ttf', 50)
    textColor = (0, 0, 0)

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.num1 = 0
        self.num2 = 0

    def reset(self):
        self.num1 = 0
        self.num2 = 0

    def roll(self, numDie = 2):
        self.num1 = random.randrange(1,7)
        self.num2 = 0
        if numDie == 2:
            self.num2 = random.randrange(1,7)
        return self.getRoll()
    
    def getRoll(self):
        return self.num1 + self.num2

    def draw(self, screen):
        rolls = f"{str(self.num1)}, {str(self.num2)}"
        rollRender = Die.font.render(rolls, True, Die.textColor)
        width = rollRender.get_rect().width
        screen.blit(rollRender, (self.x - width, self.y))
