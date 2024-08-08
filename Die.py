import random, pygame

import Globals

class Die:
    textColor = (0, 0, 0)

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.numDie = 1
        self.die = []

    def reset(self):
        self.die = []
    
    def set_num_die(self, num:int):
        self.numDie = num

    def roll(self):
        for _ in range(0, self.numDie):
            self.die.append(random.randrange(1,7))
            # self.die.append(6)
        return self.getRoll()
    
    def getRoll(self):
        return sum(self.die)

    def draw(self, screen):
        rolls = ", ".join(str(x) for x in self.die)
        rollRender = Globals.fontLg.render(rolls, True, Die.textColor)
        width = rollRender.get_rect().width
        screen.blit(rollRender, (self.x - (width/2), self.y))
