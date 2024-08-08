import pygame

import Globals

class Button:
    def __init__(self, left, top, label, padding, background, color, font=None, callback=None, *callback_args):
        self.background = background
        self.fontColor = color
        selFont = Globals.fontLg if not font else font
        self.text = selFont.render(label, True, self.fontColor)
        self.padding = padding
        self.callback = callback
        self.callback_args = callback_args

        width =  self.text.get_rect().width + 2*padding
        height = self.text.get_rect().height + padding
        x = left - width/2
        y = top
        self.rect = pygame.Rect(x, y, width, height)

    
    def draw(self, screen: pygame.Surface):
        pygame.draw.rect(screen, self.background, self.rect)
        screen.blit(self.text, (self.rect.x + self.padding, self.rect.y + self.padding/2))

    def checkClicked(self, pos):
        if self.rect.collidepoint(pos[0], pos[1]):
            if self.callback:
                self.callback(*self.callback_args)
            return True
        return False
