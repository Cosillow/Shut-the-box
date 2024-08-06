import pygame, sys
from RollMenu import RollMenu
from Box import Box
from Die import Die
from Button import Button

def killGame():
    pygame.quit()
    sys.exit()

def main():
    # General setup
    pygame.init()
    clock = pygame.time.Clock()

    # Main Window
    screen_width = 1280
    screen_height = 720
    screen = pygame.display.set_mode((screen_width,screen_height))
    pygame.display.set_caption('Shut The Box')

    # Game Objects
    bg_color = (37, 93, 20)
    box = Box(screen_width, screen_height, 12)
    rollMenu = RollMenu(screen_width, screen_height)

    # Game loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                killGame()
            if event.type == pygame.MOUSEBUTTONDOWN:
                leftClick = pygame.mouse.get_pressed()[0]
                if leftClick:
                    rollMenu.checkClicked(pygame.mouse.get_pos())
                    box.checkClicked(pygame.mouse.get_pos())

        screen.fill(bg_color)
        box.update(screen)
        rollMenu.update(screen)
        
        if box.checkWin():
            print("win")
            killGame()

        pygame.display.update()
        clock.tick(60)


if __name__ == "__main__":
    main()
