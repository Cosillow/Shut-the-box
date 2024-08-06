import pygame

class Menu:
    font = pygame.font.Font('Poppins-Regular.ttf', 50)
    textColor = (0, 0, 0)

            # if self.gameState is gameState.won or self.gameState is gameState.lost:
            # txtString = 'You win' if self.gameState is gameState.won else 'You lose'
            # winText = RollMenu.font.render(txtString, True, RollMenu.textColor)
            # width1 = winText.get_rect().width
            # screen.blit(winText, (self.screen_width / 2 - width1 / 2, self.screen_height / 2))