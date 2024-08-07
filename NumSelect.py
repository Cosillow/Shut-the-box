import pygame
from Button import Button

class NumSelect:
    font = pygame.font.Font('Poppins-Regular.ttf', 50)
    textColor = (0, 0, 0)

    def __init__(self, x, y, maxNum, minNum=1):
        self.x = x
        self.y = y
        self.selectedNum = maxNum
        self.minNum = minNum
        self.maxNum = maxNum
        self.increaseDieBtn = Button(self.x, self.y, "^", 10, (20,80,60), (0,0,0))
        self.increaseDieBtn.rect.top -= self.increaseDieBtn.rect.height
        self.decreaseDieBtn = Button(self.x, self.y + NumSelect.font.get_height(), "v", 10, (20,80,60), (0,0,0))

    def select_num(self, num):
        # keep selected within the bounds of the selector
        if num > self.maxNum or num < self.minNum:
            return
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
        renderedText = NumSelect.font.render(str(self.selectedNum), True, NumSelect.textColor)
        screen.blit(renderedText, (self.x - renderedText.get_width()/2, self.y))
