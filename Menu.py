import pygame

class Menu:
    font = pygame.font.Font('Poppins-Regular.ttf', 50)
    textColor = (0, 0, 0)
    background = (55, 55, 55)

    def __init__(self, screen_width, screen_height):
        self.screen_width = screen_width
        self.screen_height = screen_height

        pVert = 200
        width = screen_width * (2/3)
        height = screen_height - pVert*2
        self.rect = pygame.Rect((screen_width - width)/2, pVert, width, height)

    def draw(self, screen, gameOver: str=None):
            if gameOver:
                
                pygame.draw.rect(screen, Menu.background, self.rect)

                overTitle = Menu.font.render(gameOver, True, Menu.textColor)
                width1 = overTitle.get_rect().width
                screen.blit(overTitle, (self.screen_width / 2 - width1 / 2, self.screen_height / 2))
            else:
                 pass # start menu