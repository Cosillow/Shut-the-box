import pygame
pygame.font.init()

class Panel:
    # Class variables
    font = pygame.font.Font('Poppins-Regular.ttf', 32)
    textColor = (0, 0, 0)

    def __init__(self, number, left, top, width, height):
        self.number = number
        self.open = True
        self.locked = False
        self.x = left
        self.y = top
        self.width = width
        self.height = height
        self.text = Panel.font.render(str(number), True, self.textColor)

    def update(self, screen):
        pygame.draw.rect(screen, (118, 79, 25), self.get_rect())
        pWidth = self.text.get_rect().width
        screen.blit(self.text, (self.x + self.width/2 - pWidth/2, self.y))

    def get_rect(self):
        return pygame.Rect(self.x, self.y, self.width, self.height)

    def closePanel(self):
        self.text = Panel.font.render("", True, Panel.textColor)
        self.y = self.y + self.height
        self.open = False
    
    def openPanel(self):
        self.text = Panel.font.render(str(self.number), True, Panel.textColor)
        self.y = self.y - self.height
        self.open = True
    
    def checkClicked(self, pos):
        if self.locked or (not self.get_rect().collidepoint(pos[0], pos[1])):
            return
    
        if self.open:
            self.closePanel()
        else:
            self.openPanel()
