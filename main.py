import pygame, sys
from RollMenu import RollMenu
from box import Box
from die import Die
from button import Button

def killGame():
    pygame.quit()
    sys.exit()

def main():
    # General setup
    pygame.init()
    clock = pygame.time.Clock()


    # Main Window
    screen_width = 1280
    screen_height = 960
    screen = pygame.display.set_mode((screen_width,screen_height))
    pygame.display.set_caption('Shut The Box')

    # Game Objects
    bg_color = (43, 161, 90)
    box = Box(screen_width, screen_height, screen, 12)
    # die = Die(screen_width - (screen_width/4), screen_height-200, screen)
    # rollBtn1 = Button(screen_width/4, screen_height-200, "Roll 1", 15, screen, (20,80,60), (0,0,0))
    # rollBtn2 = Button(screen_width/2, screen_height-200, "Roll 2", 15, screen, (20,80,60), (0,0,0))
    # nextRoundBtn = Button(screen_width/1.25, screen_height-200, "Next", 15, screen, (20,80,60), (0,0,0))
    rollMenu = RollMenu(screen, screen_width, screen_height)

    # Game loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                killGame()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if pygame.mouse.get_pressed()[0]: # left click
                    rollMenu.checkClicked(pygame.mouse.get_pos())
                    box.checkClicked(pygame.mouse.get_pos())


        screen.fill(bg_color)
        box.update()
        
        rollMenu.update()
        
        if box.checkWin():
            pass

        pygame.display.update()
        clock.tick(60)


if __name__ == "__main__":
    main()
