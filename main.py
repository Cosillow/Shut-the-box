import pygame, sys

def killGame():
    pygame.quit()
    sys.exit()

def main():
    # General setup
    pygame.init()
    pygame.font.init()
    clock = pygame.time.Clock()
    from Menu import Menu
    from RollMenu import RollMenu
    from Box import Box

    # Main Window
    screen_width = 1280
    screen_height = 720
    screen = pygame.display.set_mode((screen_width,screen_height))
    pygame.display.set_caption('Shut The Box')

    # Game Objects
    bg_color = (37, 93, 20)
    box = Box(screen_width, screen_height, 12)
    rollMenu = RollMenu(screen_width, screen_height)
    menu = Menu(screen_width, screen_height)

    # Game loop
    while True:

        # input
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                killGame()
            if event.type == pygame.MOUSEBUTTONDOWN:
                leftClick = pygame.mouse.get_pressed()[0]
                if leftClick:
                    rollMenu.checkClicked(pygame.mouse.get_pos())
                    box.checkClicked(pygame.mouse.get_pos())
                    menu.checkClicked(pygame.mouse.get_pos())
        
        # update
        if menu.needsRestart:
            pass

        # draw
        screen.fill(bg_color)
        box.draw(screen)
        rollMenu.draw(screen)

        if box.checkWin():
            menu.draw(screen, "You Win!")
        elif box.checkLoss(rollMenu.die.getRoll()):
            menu.draw(screen, "You Lose!")

        pygame.display.update()
        clock.tick(60)


if __name__ == "__main__":
    main()
