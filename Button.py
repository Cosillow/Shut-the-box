import pygame

import Globals

class Button:
    def __init__(self, left, top, label, padding, background, font=None, isFilled=True, callback=None, *callback_args):
        self.background = background
        self.selFont = Globals.fontLg if not font else font
        self.label = label
        text = self.selFont.render(label, True, Globals.textDarkColor)
        self.padding = padding
        self.callback = callback
        self.callback_args = callback_args
        self.isFilled = isFilled

        width =  text.get_rect().width + 2*padding
        height = text.get_rect().height + padding
        x = left - width/2
        y = top
        self.rect = pygame.Rect(x, y, width, height)

    
    def draw(self, screen: pygame.Surface):
        text = self.selFont.render(self.label, True, Globals.textDarkColor)
        pygame.draw.rect(screen, self.background, self.rect, 0 if self.isFilled else 5)
        screen.blit(text, (self.rect.x + self.padding, self.rect.y + self.padding/2))

    def checkClicked(self, pos):
        if self.rect.collidepoint(pos):
            if self.callback:
                self.callback(*self.callback_args)
            return True
        return False
