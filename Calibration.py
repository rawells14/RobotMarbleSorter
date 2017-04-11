from PelletIdentifier import PelletIdentifier
from Motor import Motor
import time

m = Motor(0)
p = PelletIdentifier(0)
file = open('colordata.dat', 'w')
i = 0
while (i < 12)
    sleep(2)
    print(p.poll_color())
    file.write(str'p.poll_color()')
    sleep(1)
    m.move_motor_rel_pos(360, 150)
    i += 1
file.close()
    
