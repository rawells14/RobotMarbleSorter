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
