from panel import Panel
import pygame

class Box:
    Panels = []
    screen = None

    def __init__(self, screenWidth = None, screenHeight = None, screen = None, numPanels = 12):
        # marginLeft = 100 # give a margin of 2 Panels on each side
        if Box.Panels != []:
            return
        Box.screen = screen
        top = 100
        height = 200
        gap = 15
        error = 0.1
        width = (screenWidth - (gap*(numPanels-1 - error))) / (numPanels)

        for i in range(1, numPanels+1):
            n = i-1
            left = n*width + n*gap
            Box.Panels.append(Panel(i, left, top, width, height))
    
    def checkWin(self):
        for panel in Box.Panels:
            if not panel.locked:
                return False
        return True
    
    def checkLoss(self, roll):
        for i in range(len(Box.Panels)):
            panelL = Box.Panels[i]
            if not panelL.open:
                continue
            if panelL.number is roll:
                return False
            for j in range(i, len(Box.Panels)):
                panelR = Box.Panels[j]
                if not panelR.open:
                    continue
                if panelL.number + panelR.number is roll:
                    return False
        return True

    
    def validTurn(self, totalRolled):
        closedTotal = 0
        for panel in Box.Panels:
            if not panel.locked and not panel.open:
                closedTotal += panel.number
        return closedTotal == totalRolled
    
    def update(self):
        for Panel in Box.Panels: 
            pygame.draw.rect(Box.screen, (255,0,0), Panel.rect)
            pWidth = Panel.text.get_rect().width
            Box.screen.blit(Panel.text, (Panel.x + Panel.width/2 - pWidth/2, Panel.y))
    
    def close(self, number):
        if Box.Panels[number].open:
            if not Box.Panels[number].locked:
                Box.Panels[number].closePanel()
            else:
                print("This panel is locked")
    
    def checkClicked(self, pos):
        for Panel in Box.Panels:
            Panel.checkClicked(pos)

    def lockBox(self):
        for Panel in Box.Panels:
            if not Panel.open:
                Panel.locked = True