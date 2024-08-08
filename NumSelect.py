import pygame
from Button import Button
import Globals

class NumSelect:
    def __init__(self, x, y, maxNum, minNum=1):
        self.x = x
        self.y = y
        self.selectedNum = maxNum
        self.minNum = minNum
        self.maxNum = maxNum
        self.increaseDieBtn = Button(self.x, self.y, "^", 20, Globals.btnColor, (0,0,0), font=Globals.fontSm)
        self.increaseDieBtn.rect.top -= self.increaseDieBtn.rect.height
        self.decreaseDieBtn = Button(self.x, self.y + Globals.fontLg.get_height(), "v", 20, Globals.btnColor, (0,0,0), font=Globals.fontSm)

    def select_num(self, num):
        # keep selected within the bounds of the selector
        if num > self.maxNum or num < self.minNum:
            return
        self.selectedNum = num

    def set_max_num(self, num):
        self.maxNum = num
        self.selectedNum = num

    def checkClicked(self, position):
        if self.increaseDieBtn.checkClicked(position):
            self.select_num(self.selectedNum + 1)
            return True
        elif self.decreaseDieBtn.checkClicked(position):
            self.select_num(self.selectedNum - 1)
            return True
        return False

    def draw(self, screen):
        self.increaseDieBtn.draw(screen)
        self.decreaseDieBtn.draw(screen)
        renderedText = Globals.fontLg.render(str(self.selectedNum), True, Globals.textDarkColor)
        screen.blit(renderedText, (self.x - renderedText.get_width()/2, self.y))
