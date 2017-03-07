#! /usr/bin/env python

import time

motor_path = '/sys/class/tacho-motor/motor'
barcode_sensor_path = '/sys/class/lego-sensor/sensor2'

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
	move_motor(100, 7)
	barcode = []
	val = poll_barcode_sensor()
	while int(val)==1:
		val = poll_barcode_sensor()
	while int(val)!=1:
		val = poll_barcode_sensor()
	print(val)
	time.sleep(.45)
	move_motor(220,7)
	for i in range(0,17):
		time.sleep(.107)
		val = poll_barcode_sensor()
		print(val)
		#sometimes white is read as its color value 6 so I am changing it to 0
		if int( val ) == 6:
			val = 0
		if(i>0):
			barcode.append(int(val))
	stop(7)
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



def output_data(code):
    
    materials = ['White Glass', 'Red Glass', 'Blue Glass', 'Steel/HDPE']
    types = ['Large', 'Small']
    material_code = []
    num_pellets = ''
    for i in [2, 1, 0]:
	print(i)
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
    print(num_pellets)
    num_pellets = int(num_pellets, 2)
    print(material_needed)
    print('Decimal Number:')
    print(num_pellets)
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
        print('Type 1')
        print(type_1)
        print('Type 2')
        print(type_2)
        print(material_needed + ': ' + str(type_1) + ' ' + types[0] + ' and ' + str(type_2) + ' ' + types[1]) 
    return;



# moves the dispenser piston
# move_motor(500, 0, 1000)

# moves the barcode motor
#   move_motor(500, 1, 1000)



code = (read_barcode_auto())
print('Every other removed: ')
print(code)
colors = ['White Glass', 'Red Glass', 'Blue Glass', 'Steel/HDPE']
type = ['Large', 'Small']
color_code = []
type_code = []
for i in [2,1,0]:
	color_code.append(code[i])
for i in [7,6,5,4,3]:
	type_code.append(code[i])


print('Color code:' + str(color_code))

print('\n')
print('Type code:' + str(type_code))

output_data(code)
