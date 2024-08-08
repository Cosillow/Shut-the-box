import random, pygame

import Globals

class Die:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.numDie = 1
        self.die = []
        self.easyMode = False

    def reset(self):
        self.die = []

    def set_easy_mode(self, isEasy):
        self.easyMode = isEasy
    
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
        def helper(txt, lineNum):
            rollRender = Globals.fontLg.render(txt, True, Globals.textDarkColor)
            width = rollRender.get_rect().width
            screen.blit(rollRender, (self.x - (width/2), self.y + Globals.fontLg.get_height()*lineNum))

        rolls = ", ".join(str(x) for x in self.die)
        helper(rolls, 0)
        if self.easyMode:
            helper(f"sum: {self.getRoll()}",1)

