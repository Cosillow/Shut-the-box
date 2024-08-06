import pygame, sys

class Game:
    def __init__(self):
        # General setup
        pygame.init()
        pygame.font.init()
        self.clock = pygame.time.Clock()
        from Menu import Menu
        from RollMenu import RollMenu
        from Box import Box

        # Main Window
        screen_width = 1280
        screen_height = 720
        self.screen = pygame.display.set_mode((screen_width,screen_height))
        pygame.display.set_caption('Shut The Box')

        # Game Objects
        self.bg_color = (37, 93, 20)
        self.box = Box(screen_width, screen_height, 1)
        self.rollMenu = RollMenu(screen_width, screen_height)
        self.menu = Menu(screen_width, screen_height)

    def killGame(self):
        pygame.quit()
        sys.exit()

    def gameLoop(self):
        while True:
            # input
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.killGame()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    leftClick = pygame.mouse.get_pressed()[0]
                    if leftClick:
                        self.rollMenu.checkClicked(pygame.mouse.get_pos())
                        self.box.checkClicked(pygame.mouse.get_pos())
                        self.menu.checkClicked(pygame.mouse.get_pos())
            
            # update
            if self.menu.needsRestart:
                # restart button pressed from game loss/win
                self.rollMenu.new_game()
                self.menu.new_game()
                self.box.new_game()

            # draw
            self.screen.fill(self.bg_color)
            self.box.draw(self.screen)
            self.rollMenu.draw(self.screen)

            roll = self.rollMenu.die.getRoll()
            if self.box.checkWin(roll):
                self.menu.draw(self.screen, "You Win!")
            elif self.box.checkLoss(roll):
                self.menu.draw(self.screen, "You Lose!")

            pygame.display.update()
            self.clock.tick(60)


if __name__ == "__main__":
    g = Game()
    g.gameLoop()
