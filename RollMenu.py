from Button import Button
from Die import Die
from NumSelect import NumSelect
import Globals

class RollMenu:   
    def __init__(self, screen_width, screen_height, bx):
        self.x = screen_width/2
        self.y = screen_height-175
        self.rollBtn = Button(self.x - 100, self.y, "roll die", 15, Globals.btnColor)
        self.hasRolled = False
        from Box import Box
        self.box: Box = bx # dependency injection
        self.die = Die(self.x, self.y)
        self.recommendedDieNum = self.box.get_num_die_needed()
        self.rollSelect = NumSelect(self.x + 100, self.y, self.recommendedDieNum)

    def update(self):
        if not self.hasRolled:
            return
        ROLL = self.die.getRoll()
        SELECTED_SUM = self.box.get_selected_total()
        if SELECTED_SUM == ROLL:
            self.hasRolled = False
            self.die.reset()
            self.box.lockBox()
            
            # set roll select to recommended number
            # only on the first time the larger panels are closed
            newRecommendedDieNum = self.box.get_num_die_needed()
            if newRecommendedDieNum != self.recommendedDieNum:
                self.rollSelect.select_num(newRecommendedDieNum)
                self.recommendedDieNum = newRecommendedDieNum
        
        elif SELECTED_SUM > ROLL:
            self.box.set_illegal_selection(True)
        else: # SELECTED_SUM < ROLL
            self.box.set_illegal_selection(False)

    def new_game(self):
        self.hasRolled = False

        self.rollSelect.set_max_num(self.box.get_num_die_needed())
        self.die.reset()

    def checkClicked(self, position):
        if self.hasRolled:
            # player is thinking or finishing their turn
            return
            
        # player is about to roll
        if self.rollSelect.checkClicked(position):
            pass
        elif self.rollBtn.checkClicked(position):
            # elif prevents bubble up if button overlap
            self.die.set_num_die(self.rollSelect.selectedNum)
            ROLL = self.die.roll()
            self.hasRolled = True
            self.box.checkLoss(ROLL)
            
    def draw(self, screen):
        if self.hasRolled:
            self.die.draw(screen)
        else:
            self.rollBtn.draw(screen)
            self.rollSelect.draw(screen)
