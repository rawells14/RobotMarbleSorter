class Motor(object):
    motor_path = '/sys/class/tacho-motor/motor'

    def __init__(self, motor_number):
        self.path = motor_path + str(motor_nmber)

    def move_motor(self, speed):
        file = open(self.path + '/speed_sp', 'w')
        file.write(str(speed))
        file.close()

        file = open(self.path + '/command', 'w')
        file.write('run-forever')
        file.close()

    def move_motor_timed(self, speed, time):
        file = open(self.path + '/speed_sp', 'w')
        file.write(str(speed))
        file.close()

        file = open(self.path + '/time_sp', 'w')
        file.write(str(time))
        file.close()

        file = open(self.path + '/command', 'w')
        file.write('run-timed')
        file.close()


    def stop(self):
        file = open(self.path + '/command', 'w')
        file.write('stop')
        file.close()

    def move_motor_rel_pos(self, position, speed):
        file = open(self.path + '/position_sp', 'w')
        file.write(str(position))
        file.close

        file = open(self.path + '/stop_action', 'w')
        file.write('hold')
        file.close()

        file = open(self.path + '/speed_sp', 'w')
        file.write(str(speed));
        file.close()

        file = open(self.path + '/command', 'w')
        file.write('run-to-rel-pos')
        file.close()

    def move_motor_abs_pos(self, position, speed):
        #Should be used for pellet sorter
        file = open(self.path + '/position_sp', 'w')
        file.write(str(position))
        file.close

        file = open(self.path + '/stop_action', 'w')
        file.write('hold')
        file.close()

        file = open(self.path + '/speed_sp', 'w')
        file.write(str(speed))
        file.close()

        file = open(self.path + '/command', 'w')
        file.write('run-to-abs-pos')
        file.close()

    def pos(self):
        value = 0;
        with open(self.path + '/position', 'r') as file:
            value = file.readline()
        file.close()
        return value
