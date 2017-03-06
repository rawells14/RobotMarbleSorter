#! /usr/bin/env python

import time

motor_path = '/sys/class/tacho-motor/motor'
barcode_sensor_path = '/sys/class/lego-sensor/sensor1'

def move_motor(speed, motor_number):
    motor_number = str(motor_number)
    file = open(motor_path + motor_number + '/speed_sp', 'w')
    file.write(str(speed))
    file.close()
    
    file = open(motor_path + motor_number + '/command', 'w')
    file.write('run-forever')
    file.close()

def move_motor_timed(speed, motor_number, time):
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
    file.write('stop')
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
    move_motor_speed(200, 1, 5000)
    barcode = []
    for i in range(0, 20):
        time.sleep(.12)
        val = poll_barcode_sensor()
        print(val)
        barcode.append(int(val))
    return barcode


def read_barcode_auto():

	#wait until see a white line then switches to black line to start polling
	move_motor(100, 1)
	barcode = []
	val = poll_barcode_sensor()
	while int(val)==1:
		val = poll_barcode_sensor()
	while int(val)!=1:
		val = poll_barcode_sensor()
	print(val)
	time.sleep(.4)
	move_motor(220,1)
	for i in range(0,17):
		time.sleep(.11)
		val = poll_barcode_sensor()
		print(val)
		#sometimes white is read as its color value 6 so I am changing it to 0
		if int( val ) == 6:
			val = 0
		if(i>0):
			barcode.append(int(val))
	stop(1)
	#get rid of odd indexes to get barcode without spaces
	print(barcode)
	for i in range (0,8):
		del barcode[i]
	return barcode

def read_barcode_auto2():

	#wait until see a white line then switches to black line to start polling
	move_motor(220, 1)
	barcode = []
	val = poll_barcode_sensor()
	while int(val)==0:
		val = poll_barcode_sensor()
	stop(1)
	time.sleep(1)
	move_motor(20, 1)
	while int(val) == 1:
		val = poll_barcode_sensor()
	stop(1)
	for i in range(1,9):
                move_motor(220, 1)
		time.sleep(.125)
		stop(1)
		val = poll_barcode_sensor()
		time.sleep(1)
		print(val)
		#sometimes white is read as its color value 6 so I am changing it to 0
		if int( val ) == 6:
			val = 0
		barcode.append(int(val))
	#get rid of odd indexes to get barcode without spaces
	print(barcode)
	#for i in range (0,9):
	#	del barcode[i]
	return barcode

# moves the dispenser piston
# move_motor(500, 0, 1000)

# moves the barcode motor
#   move_motor(500, 1, 1000)

code = (read_barcode_auto())
colors = ['White Glass', 'Red Glass', 'Blue Glass', 'Steel/HDPE']
type = ['Large', 'Small']
color_code = []
type_code = []
for i in [2,1,0]:
	color_code.append(code[i])
for i in [7,6,5,4,3]:
	type_code.append(code[i])
print(color_code)
print('\n')
print(type_code)
