path = '/sys/class/tacho-motor/motor';


def move_motor(speed, motor_number, time):
    file = open(str(path + motor_number + '/speed_sp'), 'w')
    file.write(str(speed))
    file.close()

    file = open(str(path + motor_number + '/time_sp'), 'w')
    file.write(str(time))
    file.close()

    file = open(str(path + motor_number + '/command'), 'w')
    file.write('run-timed')
    file.close()


def stop(motor_number):
    file = open(str(path + motor_number + '/command'), 'w')
    file.write('')
    file.close()


move_motor(500, 2, 1000)
