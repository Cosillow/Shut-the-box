from Button import Button
import Globals

class Checkbox:
    def __init__(self, x, y, label, color, font=None):
        self.selected = False
        selFont = Globals.fontLg if not font else font

        self.labelRender = selFont.render(label, True, color)
        self.checkBtn = Button(x, y, "     ", 5, Globals.btnColor, Globals.textDarkColor, isFilled=False, font=font)
        self.gap = 20
        self.labelPos = (self.checkBtn.rect.left - self.labelRender.get_width() - self.gap, self.checkBtn.rect.y)
        totalWidth = self.gap + self.labelRender.get_rect().width + self.checkBtn.rect.width
        self.labelPos = (self.labelPos[0] + totalWidth/2, self.labelPos[1])
        self.checkBtn.rect.x += totalWidth/2

    def __box_clicked(self):
        self.selected = not self.selected
        self.checkBtn.isFilled = self.selected

    def is_selected(self):
        return self.selected
    
    def checkClicked(self, pos):
        labelRect = self.labelRender.get_rect()
        labelRect.x, labelRect.y = self.labelPos
        labelRect.w += self.gap
        if self.checkBtn.checkClicked(pos) or labelRect.collidepoint(pos):
            self.__box_clicked()

    def draw(self, screen):
        self.checkBtn.draw(screen)
        screen.blit(self.labelRender, self.labelPos)
