class Sorter(object):
        positions = []
        colors = []
        def __init__(self, conveyer_number, popper_number):
            self.conveyer_motor = Motor(conveyer_number)
            self.popper_motor = Motor(popper_number)

        def pop():
            self.popper_motor.move_motor_abs_pos(-75, 1000)
            time.sleep(1)
            self.popper_motor.move_motor_abs_pos(0, 1000)


        def move_to_marble(color):
            for i in range(len(colors)):
                if colors[i] == color:
                    self.conveyer_motor.move_motor_abs_pos(positions[i], 100)
                    return
            print('Couldn\'t find color)

        def pop_marble(color):
            move_to_marble(color)
            time.sleep(5)
            pop()
