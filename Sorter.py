class Sorter(object):
        positions = []

        def __init__(self, conveyer_number, popper_number):
            self.conveyer_motor = Motor(conveyer_number)
            self.popper_motor = Motor(popper_number)

        def pop():
            motor.move_motor_abs_pos(-75, 1000)
            time.sleep(2)
            motor.move_motor_abs_pos(0, 1000)
