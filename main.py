import pygame, sys
from enum import IntEnum

class GameState(IntEnum):
    Playing = 0
    Won = 1
    Loss = 2

class Game:
    def __init__(self):
        pygame.init()
        pygame.font.init()
        self.clock = pygame.time.Clock()
        from Menu import Menu
        from Box import Box
        from Button import Button
        import Globals

        screen_width = 1280
        screen_height = 720
        self.screen = pygame.display.set_mode((screen_width,screen_height))
        pygame.display.set_caption('Shut The Box')

        self.feltColor = (37, 93, 20)
        self.box = Box(screen_width, screen_height, 12)
        self.menu = Menu(screen_width, screen_height, self)
        self.exitBtn = Button(0, screen_height, "exit", 15, (20,80,60), (0,0,0), callback=self.menu.go_to_main_menu, font=Globals.fontMd)
        self.exitBtn.rect.x = self.exitBtn.rect.x + (self.exitBtn.rect.width/2)
        self.exitBtn.rect.y = self.exitBtn.rect.y - (self.exitBtn.rect.height)

    def killGame(self):
        pygame.quit()
        sys.exit()

    def restart_game(self, panelNum=None):
        print("restarting game")
        self.box.new_game(panelNum)
        self.menu.isMainMenu = False

    def update(self):
        self.box.update()            
    
    def draw(self):
        if self.menu.isMainMenu:
            self.screen.fill((0,0,0))
            self.menu.draw(self.screen)
        else:
            self.screen.fill(self.feltColor)
            self.box.draw(self.screen)    

            gameState = self.box.get_game_state()
            if gameState == GameState.Won:
                self.menu.draw(self.screen, "You Win!")
            elif gameState == GameState.Loss:
                self.menu.draw(self.screen, "You Lose!")
            else:
                self.exitBtn.draw(self.screen)

        pygame.display.update()

    def gameLoop(self):
        while True:
            # input
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.killGame()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    leftClick = pygame.mouse.get_pressed()[0]
                    if leftClick:
                        gameState = self.box.get_game_state()
                        if not (gameState == GameState.Playing) or self.menu.isMainMenu:
                            self.menu.checkClicked(pygame.mouse.get_pos())
                        elif gameState == GameState.Playing:
                            self.box.checkClicked(pygame.mouse.get_pos())
                            self.exitBtn.checkClicked(pygame.mouse.get_pos())
            
            self.update()
            self.draw()
            
            self.clock.tick(60)


if __name__ == "__main__":
    g = Game()
    g.gameLoop()
