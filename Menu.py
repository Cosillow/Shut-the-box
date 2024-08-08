import pygame, math

from Button import Button
from Checkbox import Checkbox
import Globals
from NumSelect import NumSelect

class Menu:
    background = (55, 55, 55)

    def __init__(self, screen_width, screen_height, gm):
        self.isMainMenu = True
        marginVert = 200
        width = screen_width * (2/3)
        height = screen_height - marginVert*2
        self.rect = pygame.Rect((screen_width - width)/2, marginVert, width, height)
        self.restartBtn = Button(self.rect.centerx-200, self.rect.bottom-130, "play", 15, Globals.btnColor)
        self.mainMenuBtn = Button(self.rect.centerx+200, self.rect.bottom-130, "main menu", 15, Globals.btnColor)
        self.panelSelect = NumSelect(self.rect.centerx + 200, self.rect.centery, 36)
        self.panelSelect.select_num(12)
        self.easyModeChkbox = Checkbox(screen_height - 100, self.rect.centerx, "Easy Mode:", Globals.textLightColor, Globals.fontMd)
        from main import Game
        self.game: Game = gm # dependency injection

    def draw(self, screen, gameOver:str = None):
            pygame.draw.rect(screen, Menu.background, self.rect)

            if gameOver:
                titleRender = Globals.fontLg.render(gameOver, True, Globals.textDarkColor)
                self.mainMenuBtn.draw(screen)
            else:
                titleRender = Globals.fontLg.render("New Game", True, Globals.textDarkColor)
                self.panelSelect.draw(screen)
                largestRoll = math.ceil(self.panelSelect.selectedNum / 6) * 6
                prob = f"you have a {math.pow((1/6), (largestRoll/6)):%} chance to roll a {largestRoll}"
                probRender = Globals.fontSm.render(prob, True, Globals.textLightColor)
                probRect = probRender.get_rect()
                screen.blit(probRender, (self.rect.centerx - (probRect.width / 2), self.rect.bottom+probRect.height))
                self.easyModeChkbox.draw(screen)
            
            self.restartBtn.draw(screen)
            width1 = titleRender.get_rect().width
            screen.blit(titleRender, (self.rect.centerx - (width1 / 2), self.rect.top + 20))
            
    def go_to_main_menu(self):
        self.isMainMenu = True
    
    def checkClicked(self, position):
        if self.isMainMenu and self.panelSelect.checkClicked(position):
            pass
        elif self.isMainMenu and self.easyModeChkbox.checkClicked(position):
            pass
        elif (not self.isMainMenu) and self.mainMenuBtn.checkClicked(position):
            self.go_to_main_menu()
        elif self.restartBtn.checkClicked(position):
            print(self.panelSelect.selectedNum)
            if self.isMainMenu:
                self.game.restart_game(self.panelSelect.selectedNum)
                self.game.box.rollMenu.die.set_easy_mode(self.easyModeChkbox.is_selected())
            else: 
                self.game.restart_game()
