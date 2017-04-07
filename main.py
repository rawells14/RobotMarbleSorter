#!/usr/bin/env python
import time
from Motor import Motor
motor = Motor(2)

motor.move_motor_abs_pos(-75, 1000)
time.sleep(2)
motor.move_motor_abs_pos(0, 1000)
