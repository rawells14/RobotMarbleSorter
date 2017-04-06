import time
sensor_path = '/sys/class/lego-sensor/sensor'
class Barcode(object):
    def __init__(self, sensor_number, motor_number):
        self.path = sensor_path + str(sensor_number)
        self.motor_number = motor_number

    def poll(self):
        value = 0
        file = open(self.path + '/mode', 'w')
        file.write('COL-COLOR')
        file.close()
        with open(self.path + '/value0', 'r') as file:
            value = file.readline()
        file.close()
        return value

    def read_barcode(self):
        code = []
        i = 0
        barcode_motor = Motor(self.motor_number)
        while i < 100:
            code.append(self.poll)
            code.append(barcode_motor.pos)
            barcode_motor.move_motor_rel_pos(20, 150)
        return code

    def process_code(self, code):
        #FIX ME: need to process data from scan and transform into number and type of marbles
        print('HI')
