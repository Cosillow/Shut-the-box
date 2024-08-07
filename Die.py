import random, pygame

class Die:
    font = pygame.font.Font('Poppins-Regular.ttf', 50)
    textColor = (0, 0, 0)

    def __init__(self, x, y, maxDie):
        self.x = x
        self.y = y
        self.maxDie = maxDie
        self.currDie = maxDie
        self.die = []

    def reset(self):
        self.die = []

    def set_max_die(self, maxDie):
        self.maxDie = maxDie
    
    def adjust_curr_die(self, adj:int):
        newDie = self.currDie + adj
        if newDie > 0 and newDie <= self.maxDie:
            self.currDie = newDie

    def roll(self):
        for _ in range(0, self.currDie):
            self.die.append(random.randrange(1,7))
            # self.die.append(6)
        return self.getRoll()
    
    def getRoll(self):
        return sum(self.die)

    def draw(self, screen):
        rolls = ", ".join(str(x) for x in self.die)
        rollRender = Die.font.render(rolls, True, Die.textColor)
        width = rollRender.get_rect().width
        screen.blit(rollRender, (self.x - width, self.y))
