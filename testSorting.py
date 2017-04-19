#!/usr/bin/env python3
#from ev3dev.ev3 import *
import time
from Motor import Motor
from Barcode import Barcode
from Sorter import Sorter
from PelletIdentifier import PelletIdentifier
from Color import Color

totalMarbles = [0,0,0,0,0,0,0,0]
totalDosage = [0,0,3,0,0,1,0,1]
pelletReader = PelletIdentifier(0)
sorter = Sorter(1, 2)
piston = Motor(0)

#start sorting process
#wait until there is a marble to read
while (not(pelletReader.isMarble())):
	continue

#once marble is found continue reading marbles until the box is seen again
while(pelletReader.isMarble()):
    marbleNum = -1
    marbleNum = pelletReader.identify()
    #if it was not in any range, put it in the trash bin
    if (marbleNum < 0):
        marbleNum = 8
    #if it was the color of the box, continue
    elif(marbleNum > 7):
        continue
    #if it was an actual marble, add to the total number of marbles of that type
    else:
        totalMarbles[marbleNum] += 1
    sorter.move_to_marble_num(marbleNum)
	print(marbleNum)
	time.sleep(1)
    piston.move_motor_rel_pos(360, 500)
    print(totalMarbles)
    #NEED TO PLAY WITH THIS NUMBER BECAUSE TIMING OF PISTON WILL BE CONSTANT AND IDK
    #HOW LONG THIS WHOLE PROCESS WILL TAKE
    time.sleep(4)
canDispense = True
for i in range(0, 7):
    if (totalMarbles[i] < totalDosage[i]):
        canDispense = False

#if we have enough marbles
if(canDispense):
    for i in range(0,7):
        if(totalDosage[i] == 0):
            continue
        else:
            for j in range(1, totalDosage[i]):
                sorter.pop_marble_num(i)
#if we cannot dispense because there are not enough marbles in the sorter
else:
	Sound.beep()
