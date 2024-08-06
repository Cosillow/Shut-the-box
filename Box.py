from Panel import Panel
import pygame

class Box:
    # class variable ensures only one list of panels exists (similar to a singleton)
    # allows other classes to check statuses of the box
    Panels: list[Panel] = []

    def __init__(self, screenWidth = None, screenHeight = None, numPanels = 12):
        # marginLeft = 100 # give a margin of 2 Panels on each side
        if Box.Panels != []:
            return
        top = 50
        height = 200
        gap = 15
        error = 0.1
        width = (screenWidth - (gap*(numPanels-1 - error))) / (numPanels)

        for i in range(1, numPanels+1):
            n = i-1
            left = n*width + n*gap
            Box.Panels.append(Panel(i, left, top, width, height))
    
    def new_game(self):
        self.lockBox(False)
        for p in Box.Panels:
            p.openPanel()
        

    def checkWin(self, roll):
        sumDown = 0
        for panel in Box.Panels:
            if panel.open:
                return False
            if not panel.open and not (panel.locked):
                sumDown += panel.number
        return sumDown == roll
    
    def checkLoss(self, roll=None):
        # two sum O(N) soln
        if not roll:
            return False
        
        map = dict()
        found = True
        for i, p in enumerate(Box.Panels):
            if p.locked:
                continue
            if p.number > roll:
                break

            if p.number == roll:
                # TODO: adjust panel visual for possible choices
                found = False
                continue
            elif p.number in map:
                # TODO: adjust both panels' visual for possible choices
                found = False
            else:
                map[roll - p.number] = i
        return found

    def validTurn(self, totalRolled):
        closedTotal = 0
        for panel in Box.Panels:
            if not panel.locked and not panel.open:
                closedTotal += panel.number
        return closedTotal == totalRolled
    
    def draw(self, screen):
        for p in Box.Panels:
            p.draw(screen)
    
    def close(self, number):
        if Box.Panels[number].open:
            if not Box.Panels[number].locked:
                Box.Panels[number].closePanel()
            else:
                print("This panel is locked")
    
    def checkClicked(self, pos):
        for Panel in Box.Panels:
            Panel.checkClicked(pos)

    def lockBox(self, lock=True):
        for Panel in Box.Panels:
            if not Panel.open:
                Panel.locked = lock