import pygame, sys
from enum import IntEnum

class GameState(IntEnum):
    Playing = 0
    Won = 1
    Loss = 2

class Game:
    def __init__(self):
        # General setup
        pygame.init()
        pygame.font.init()
        self.clock = pygame.time.Clock()
        from Menu import Menu
        from Box import Box

        # Main Window
        screen_width = 1280
        screen_height = 720
        self.screen = pygame.display.set_mode((screen_width,screen_height))
        pygame.display.set_caption('Shut The Box')

        # Game Objects
        self.bg_color = (37, 93, 20)
        self.box = Box(screen_width, screen_height, 20)
        self.menu = Menu(screen_width, screen_height)

    def killGame(self):
        pygame.quit()
        sys.exit()

    def update(self):
        self.box.update()
        if self.menu.needsRestart:
            # restart button pressed from game loss/win
            self.menu.new_game()
            self.box.new_game()
    
    def draw(self):
        self.screen.fill(self.bg_color)
        self.box.draw(self.screen)

        gameState = self.box.get_game_state()
        if gameState == GameState.Won:
            self.menu.draw(self.screen, "You Win!")
        elif gameState == GameState.Loss:
            self.menu.draw(self.screen, "You Lose!")

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
                        self.box.checkClicked(pygame.mouse.get_pos())
                        if not (self.box.get_game_state() == GameState.Playing):
                            self.menu.checkClicked(pygame.mouse.get_pos())
            
            self.update()
            self.draw()
            
            self.clock.tick(60)


if __name__ == "__main__":
    g = Game()
    g.gameLoop()
