import pygame

class Panel:
    # Class variables
    font = pygame.font.Font('Poppins-Regular.ttf', 32)

    def __init__(self, number, left, top, width, height):
        self.number = number
        self.open = True
        self.locked = False
        self.x = left
        self.y = top
        self.width = width
        self.height = height
        self.textColor = (0, 0, 0)
        self.text = Panel.font.render(str(number), True, self.textColor)

    def draw(self, screen):
        pygame.draw.rect(screen, (118, 79, 25), self.get_rect())
        pWidth = self.text.get_rect().width
        screen.blit(self.text, (self.x + self.width/2 - pWidth/2, self.y))

    def get_rect(self):
        return pygame.Rect(self.x, self.y, self.width, self.height)

    def closePanel(self):
        if not self.open:
            return
        self.text = Panel.font.render("", True, self.textColor)
        self.y = self.y + self.height - 20
        self.open = False
    
    def openPanel(self):
        if self.open:
            return
        self.text = Panel.font.render(str(self.number), True, self.textColor)
        self.y = self.y - self.height + 20
        self.open = True
    
    def checkClicked(self, pos):
        if self.locked or (not self.get_rect().collidepoint(pos[0], pos[1])):
            return
    
        if self.open:
            self.closePanel()
        else:
            self.openPanel()
