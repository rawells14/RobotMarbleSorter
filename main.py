#!/usr/bin/env python
import time
from Motor import Motor
from Barcode import Barcode
from Sorter import Sorter

#motor = Motor(2)
#motor.move_motor_abs_pos(0, 100)

#time.sleep(1)

sorter = Sorter(0, 1)
sorter.pop_marble_num(8)


#motor.move_motor_abs_pos(0, 100)
# b = Barcode(2, 0)
# b.read_barcode()
