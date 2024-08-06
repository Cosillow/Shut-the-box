import pygame

from Button import Button

class Menu:
    font = pygame.font.Font('Poppins-Regular.ttf', 50)
    textColor = (0, 0, 0)
    background = (55, 55, 55)

    def __init__(self, screen_width, screen_height):
        self.needsRestart = False

        pVert = 200
        width = screen_width * (2/3)
        height = screen_height - pVert*2
        self.rect = pygame.Rect((screen_width - width)/2, pVert, width, height)

        self.restartBtn = Button(self.rect.centerx, self.rect.bottom-130, "restart", 15, (20,80,60), (0,0,0))

    def new_game(self):
        self.needsRestart = False

    def draw(self, screen, gameOver: str=None):
            if gameOver:
                
                pygame.draw.rect(screen, Menu.background, self.rect)

                overTitle = Menu.font.render(gameOver, True, Menu.textColor)
                width1 = overTitle.get_rect().width
                screen.blit(overTitle, (self.rect.centerx - (width1 / 2), self.rect.top))
                self.restartBtn.draw(screen)
            else:
                 pass # start menu
            
    def checkClicked(self, position):
        if self.restartBtn.checkClicked(position):
            self.needsRestart = True
