import pygame

import Globals

class Panel:
    # Class variables
    normalColor = (118, 79, 25)
    legalColor = (73, 118, 25)
    illegalColor = (118, 54, 25)

    def __init__(self, number, left, top, width, height):
        self.number = number
        self.open = True
        self.locked = False
        self.x = left
        self.y = top
        self.width = width
        self.height = height
        self.text = Globals.fontMd.render(str(number), True, Globals.textDarkColor)
        self.illegal = False

    def draw(self, screen):
        isSelected = (not self.open) and (not self.locked)
        color = Panel.legalColor if isSelected and not self.illegal  \
                else Panel.illegalColor if isSelected and self.illegal \
                else Panel.normalColor 
        pygame.draw.rect(screen, color, self.get_rect())
        pWidth = self.text.get_rect().width
        screen.blit(self.text, (self.x + self.width/2 - pWidth/2, self.y))

    def lock(self, isLock):
        self.locked = isLock
        self.illegal = self.locked

    def get_rect(self):
        return pygame.Rect(self.x, self.y, self.width, self.height)

    def closePanel(self):
        if not self.open:
            return
        self.text = Globals.fontMd.render("", True, Globals.textDarkColor)
        self.y = self.y + self.height - 20
        self.open = False
    
    def openPanel(self):
        if self.open:
            return
        self.text = Globals.fontMd.render(str(self.number), True, Globals.textDarkColor)
        self.y = self.y - self.height + 20
        self.open = True
    
    def checkClicked(self, pos):
        if self.locked or (not self.get_rect().collidepoint(pos[0], pos[1])):
            return
    
        if self.open:
            self.closePanel()
        else:
            self.openPanel()
