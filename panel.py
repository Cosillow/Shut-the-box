import pygame
pygame.font.init()

class Panel:
    # Class variables
    font = pygame.font.Font('Poppins-Regular.ttf', 32)
    textColor = (18, 0, 246)

    def __init__(self, number, left, top, width, height):
        self.number = number
        self.open = True
        self.locked = False
        self.x = left
        self.y = top
        self.width = width
        self.height = height
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.text = Panel.font.render(str(number), True, self.textColor)

    def closePanel(self):
        self.text = Panel.font.render("clicked", True, Panel.textColor)
        self.open = False
    
    def openPanel(self):
        self.text = Panel.font.render(str(self.number), True, Panel.textColor)
        self.open = True
    
    def checkClicked(self, pos):
        if self.rect.collidepoint(pos[0], pos[1]):
            # panel has been clicked
            if not self.locked:
                if self.open:
                    self.closePanel()
                else:
                    self.openPanel()
