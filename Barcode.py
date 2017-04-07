import time
from Motor import Motor

class Barcode(object):
    def __init__(self, sensor_number, motor_number):
        self.sensor_path = '/sys/class/lego-sensor/sensor'
        self.path = self.sensor_path + str(sensor_number)
        self.motor_number = motor_number

    def poll(self):
        value = 0
        file = open(self.path + '/mode', 'w')
        file.write('COL-COLOR')
        file.close()
        with open(self.path + '/value0', 'r') as file:
            value = file.readline().replace('\n', '')
        file.close()
        return value

    def read_barcode(self):
        code = []
        i = 0
        barcode_motor = Motor(self.motor_number)

        # finds start of barcode
        is_start_of_barcode = False
        while not(is_start_of_barcode):
            barcode_motor.move_motor(25)
            print(self.poll())
            if (self.poll() == '1' or self.poll() == '7'):
                print('Found barcode')
                is_start_of_barcode = True

        # reads barcode
        while i < 8:
            code.append(self.poll())
            barcode_motor.move_motor_rel_pos(54, 100)
            print(code[i])
            i+=1
            time.sleep(1)
        return code

    def process_code(self, code):
        #FIX ME: need to process data from scan and transform into number and type of marbles
        print('HI')

b = Barcode(1, 0)
b.read_barcode()
