import math, pygame
from Panel import Panel
from RollMenu import RollMenu
from main import GameState

class Box:
    def __init__(self, screenWidth = None, screenHeight = None, numPanels = 12):
        self.gameState: GameState = GameState.Playing
        self.Panels: list[Panel] = []

        top = 50
        height = 200
        gap = 5
        error = 0.1
        width = (screenWidth - (gap*(numPanels-1 - error))) / (numPanels)

        for i in range(1, numPanels+1):
            n = i-1
            left = n*width + n*gap
            self.Panels.append(Panel(i, left, top, width, height))
            
        self.rollMenu = RollMenu(screenWidth, screenHeight, self)
    
    def update(self):
        if not (self.gameState == GameState.Playing):
            return
        self.rollMenu.update()
        roll = self.rollMenu.die.getRoll()
        if self.checkWin(roll):
            self.gameState = GameState.Won

    def new_game(self):
        self.gameState = GameState.Playing
        self.rollMenu.new_game()
        self.lockBox(False)
        for p in self.Panels:
            p.openPanel()
        

    def checkWin(self, roll):
        sumDown = 0
        for panel in self.Panels:
            if panel.open:
                return False
            if not panel.open and not (panel.locked):
                sumDown += panel.number
        return sumDown == roll
    
    def checkLoss(self, roll=None):
        # finds all sums of any combination of panels (p)
        # O(2^p) backtracking solution

        if not roll:
            return False
        
        res = []
        it = 0
        def dfs(i, curr, total):
            nonlocal it
            it += 1
            
            if total == roll:
                res.append(curr.copy())
                return
            panelNum = i + 1
            if i >= len(self.Panels) or panelNum > roll or total > roll:
                return
            
            if self.Panels[i].locked:
                # skip panel
                dfs(i + 1, curr, total)
                return

            # use this panel
            curr.append(panelNum)
            dfs(i + 1, curr, total + panelNum)

            # don't use this panel
            curr.pop()
            dfs(i + 1, curr, total)

        dfs(0, [], 0)
        print(f"in {it} iterations, {len(res)} results were found: {res}")
        # TODO: adjust all panel visuals for possible choices
        if not res:
            self.gameState = GameState.Loss
        
    # def two_sum(self, roll):
    #     map = dict()
    #     for i, p in enumerate(self.Panels):
    #         if p.locked:
    #             continue
    #         if p.number > roll:
    #             break

    #         if p.number == roll:
    #             return False
    #         elif p.number in map:
    #             return False
    #         else:
    #             map[roll - p.number] = i
    #     return True

    def validTurn(self, totalRolled):
        closedTotal = 0
        for panel in self.Panels:
            if not panel.locked and not panel.open:
                closedTotal += panel.number
        return closedTotal == totalRolled
    
    def get_game_state(self):
        return self.gameState

    def draw(self, screen):
        for p in self.Panels:
            p.draw(screen)
        self.rollMenu.draw(screen)
        
    def checkClicked(self, pos):
        self.rollMenu.checkClicked(pygame.mouse.get_pos())
        for Panel in self.Panels:
            Panel.checkClicked(pos)

    def lockBox(self, lock=True):
        for Panel in self.Panels:
            if not Panel.open:
                Panel.locked = lock

    def get_num_die_needed(self) -> int:
        largest = 1
        for p in reversed(self.Panels):
            if not p.locked:
                largest = p.number
                break
        return math.ceil(largest / 6)
