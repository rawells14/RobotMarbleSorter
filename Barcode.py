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
        while i < 9:
            barcode_motor.move_motor_rel_pos(53, 100)
            code.append(self.poll())
            print(code[i])
            i+=1
            time.sleep(1)

        return code

    def process_code(self, code):
        materials = ['White Glass', 'Red Glass', 'Blue Glass', 'Steel/HDPE']
        types = ['Large', 'Small']
        material_code = []
        num_pellets = ''
        for i in [2, 1, 0]:
            material_code.append(code[i])
        for i in [7,6,5,4,3]:
            num_pellets += str(code[i])
        material_needed = 'Not Detected'
        if(material_code == [0, 0, 1]):
            material_needed = materials[0]
        elif(material_code == [0, 1, 0]):
            material_needed = materials[1]
        elif(material_code == [0, 1, 1]):
            material_needed = materials[2]
        elif(material_code == [1, 0, 0]):
            material_needed = materials[3]
            types[0] = 'Steel'
            types[1] = 'HDPE'
        num_pellets = int(num_pellets, 2)
        print(material_needed)
        type_1 = 0
        type_2 = 0
        for i in range(1, num_pellets):
            type_1 += 1
            if(type_1 % 4 == 0):
                type_1 = 0
                type_2 += 1
        if(type_1 > 3 and type_2 > 3):
            print('Impossible amount of marbles')
        else:
            print(material_needed + ': ' + str(type_1) + ' ' + types[0] + ' and ' + str(type_2) + ' ' + types[1])
        return
