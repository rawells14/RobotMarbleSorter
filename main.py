def move_motor(speed, motor_number, time):
    file = open('/sys/class/tacho-motor/motor' + motor_number + '/speed_sp', 'w')
    file.write(str(speed))
    file.close()

    file = open('/sys/class/tacho-motor/motor' + motor_number + '/time_sp', 'w')
    file.write(str(time))
    file.close()

    file = open('/sys/class/tacho-motor/motor' + motor_number + '/command', 'w')
    file.write('run-timed')
    file.close()


def stop(motor_number):
    file = open('/sys/class/tacho-motor/motor' + motor_number + '/command', 'w')
    file.write('')
    file.close()


move_motor(500)
