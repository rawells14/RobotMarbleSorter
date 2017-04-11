
class Motor(object):


    def __init__(self, motor_number):
        self.motor_path = '/sys/class/tacho-motor/motor'
        self.path = self.motor_path + str(motor_number)

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
<<<<<<< HEAD:Motor.py

    def move_motor_rel_pos(self, position, speed):
=======
        
    def move_motor_pos(self, position):
        #FIX ME: need to figure out how to set to move to
        #        relative position to work with the rest of the code
>>>>>>> parent of 9600c13... Added move to absolute position function:mainWithUntestedUpdates.py
        file = open(self.path + '/position_sp', 'w')
        file.write(str(position))
        file.close

        file = open(self.path + '/stop_action', 'w')
        file.write('hold')
        file.close()

        file = open(self.path + '/command', 'w')
        file.write('run-to-rel-pos')
        file.close()

    def pos(self):
        value = 0;
        with open(self.path + '/position', 'r') as file:
            value = file.readline()
        file.close()
        return value
