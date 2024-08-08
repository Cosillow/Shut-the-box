import pygame, math

from Button import Button
from NumSelect import NumSelect

class Menu:
    font = pygame.font.Font('Poppins-Regular.ttf', 50)
    textColor = (0, 0, 0)
    background = (55, 55, 55)

    def __init__(self, screen_width, screen_height, gm):
        self.isMainMenu = True
        marginVert = 200
        width = screen_width * (2/3)
        height = screen_height - marginVert*2
        self.rect = pygame.Rect((screen_width - width)/2, marginVert, width, height)
        self.restartBtn = Button(self.rect.centerx-200, self.rect.bottom-130, "play", 15, (20,80,60), (0,0,0))
        self.mainMenuBtn = Button(self.rect.centerx+200, self.rect.bottom-130, "main menu", 15, (20,80,60), (0,0,0))
        self.panelSelect = NumSelect(self.rect.centerx + 200, self.rect.centery, 36)
        self.panelSelect.select_num(12)
        from main import Game
        self.game: Game = gm # dependency injection

    def draw(self, screen, gameOver:str = None):
            pygame.draw.rect(screen, Menu.background, self.rect)

            if gameOver:
                titleRender = Menu.font.render(gameOver, True, Menu.textColor)
                self.mainMenuBtn.draw(screen)
            else:
                titleRender = Menu.font.render("New Game", True, Menu.textColor)
                self.panelSelect.draw(screen)
                largestRoll = math.ceil(self.panelSelect.selectedNum / 6) * 6
                prob = f"you have a {math.pow((1/6), (largestRoll/6)):%} chance to roll a {largestRoll}"
                probRender = Menu.font.render(prob, True, (100,100,100))
                probRect = probRender.get_rect()
                screen.blit(probRender, (self.rect.centerx - (probRect.width / 2), self.rect.bottom+probRect.height))
            
            self.restartBtn.draw(screen)
            width1 = titleRender.get_rect().width
            screen.blit(titleRender, (self.rect.centerx - (width1 / 2), self.rect.top + 20))
            
    def go_to_main_menu(self):
        self.isMainMenu = True
    
    def checkClicked(self, position):
        if self.isMainMenu and self.panelSelect.checkClicked(position):
            pass
        elif (not self.isMainMenu) and self.mainMenuBtn.checkClicked(position):
            self.go_to_main_menu()
        elif self.restartBtn.checkClicked(position):
            print(self.panelSelect.selectedNum)
            self.game.restart_game(self.panelSelect.selectedNum) if self.isMainMenu else self.game.restart_game()
