#! /usr/bin/env python

import time

motor_path = '/sys/class/tacho-motor/motor'
barcode_sensor_path = '/sys/class/lego-sensor/sensor1'

def move_motor(speed, motor_number, time):
    motor_number = str(motor_number)
    file = open(motor_path+ motor_number + '/speed_sp', 'w')
    file.write(str(speed))
    file.close()

    file = open(motor_path + motor_number + '/time_sp', 'w')
    file.write(str(time))
    file.close()

    file = open(motor_path + motor_number + '/command', 'w')
    file.write('run-timed')
    file.close()


def stop(motor_number):
    motor_number = str(motor_number)
    file = open(motor_path + motor_number + '/command', 'w')
    file.write('')
    file.close()

def poll_barcode_sensor():
    value = 0
    file = open(barcode_sensor_path + '/mode', 'w')
    file.write('COL-COLOR')
    file.close()
    with open(barcode_sensor_path + '/value0', 'r') as file:
        value = file.readline()
    file.close()
    return value

def read_barcode():

    # 20 total binary values
    move_motor(100, 1, 9000)
    barcode = []
    for i in range(0, 20):
        time.sleep(.2)
        val = poll_barcode_sensor()
        print(val)
        barcode.append(int(val))
    return barcode

# moves the dispenser piston
# move_motor(500, 0, 1000)

# moves the barcode motor
#   move_motor(500, 1, 1000)

print(read_barcode())

