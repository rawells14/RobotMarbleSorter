motor_path = '/sys/class/tacho-motor/motor'


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

move_motor(500, 1, 1000)
move_motor(500, 2, 1000)