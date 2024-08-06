import pygame
pygame.font.init()

class Button:
    # Class variables
    font = pygame.font.Font('Poppins-Regular.ttf', 50)

    def __init__(self, left, top, label, padding, background, color):
        self.background = background
        self.fontColor = color
        self.text = Button.font.render(label, True, self.fontColor)
        self.width =  self.text.get_rect().width + 2*padding
        self.height = self.text.get_rect().height + padding
        self.padding = padding
        self.x = left - self.width/2
        self.y = top
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)

    
    def update(self, screen):
        pygame.draw.rect(screen, self.background, self.rect)
        screen.blit(self.text, (self.x + self.padding, self.y + self.padding/2))

    def checkClicked(self, pos):
        if self.rect.collidepoint(pos[0], pos[1]):
            return True
        return False