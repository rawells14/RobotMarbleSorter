from Motor import Motor
import time
class Sorter(object):

        def __init__(self, conveyer_number, popper_number):
            self.positions = [0, -180, -63, -290, 91, 176, 274, 336, 397]
            self.colors = ['small blue', 'small red', 'large blue', 'large red', 'large white', 'small white', 'hdpe', 'steel', 'trash']
            self.newPostitionOrder = [336, 274, 176, 91, 0, -63, -180, -290, 397]
            self.newColorsOrder = ['Steel', 'HDPE', 'small white', 'large white', 'small blue', 'large blue',
                                'small red', 'large red', 'trash']
            self.conveyerSpeed = 350
            self.conveyer_motor = Motor(conveyer_number)
            self.popper_motor = Motor(popper_number)

        def pop(self):
            self.popper_motor.move_motor_abs_pos(-100, 1000)
            time.sleep(1)
            self.popper_motor.move_motor_abs_pos(0, 1000)

        def move_to_marble_num(self, marbleNum):
            self.conveyer_motor.move_motor_abs_pos(self.newPostitionOrder[marbleNum], self.conveyerSpeed)

        def pop_marble_num(self, marbleNum):
            self.move_to_marble_num(marbleNum)
            time.sleep(2)
            self.pop()
            time.sleep(1)   

        def move_to_marble(self, color):
            for i in range(len(self.colors)):
                if self.colors[i] == color:
                    self.conveyer_motor.move_motor_abs_pos(self.positions[i], 350)
                    return
            print('Couldn\'t find color')

        def go_back_to_middle(self):
            self.conveyer_motor.move_motor_abs_pos(0, 500)

        def pop_marble(self, color):
            self.move_to_marble(color)
            time.sleep(4)
            self.pop()
            time.sleep(1)
            self.go_back_to_middle
