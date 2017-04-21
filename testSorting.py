#!/usr/bin/env python3
#from ev3dev.ev3 import *
import time
from Motor import Motor
from Barcode import Barcode
from Sorter import Sorter
from PelletIdentifier import PelletIdentifier
from Color import Color

#to be added to when marble is sorted into bin in sorter order
totalMarbles = [0,0,0,0,0,0,0,0]
#to be added to when barcode is read in sorter order
totalDosage = [0,0,0,2,0,0,0,0]

barcodeReader = Barcode(0,1)
pelletReader = PelletIdentifier(1)
sorter = Sorter(0, 3)
piston = Motor(2)


#start sorting process
#wait until there is a marble to read
while (not(pelletReader.isMarble())):
    continue

#once marble is found continue reading marbles until the box is seen again
i = 0
while(not(pelletReader.isMarble()) or i < 4):
    marbleNum = -1
    marbleNum = pelletReader.identify()
    #if it was not in any range, put it in the trash bin
    if (marbleNum < 0):
        marbleNum = 8
        print(marbleNum)
    #if it was the color of the box, continue
    elif(marbleNum > 7):
        continue
    #if it was an actual marble, add to the total number of marbles of that type
    else:
        print(marbleNum)
        totalMarbles[marbleNum] += 1
    sorter.move_to_marble_num(marbleNum)
    time.sleep(2)
    piston.move_motor_rel_pos(360, 500)
    i += 1

    #NEED TO PLAY WITH THIS NUMBER BECAUSE TIMING OF PISTON WILL BE CONSTANT AND IDK
    #HOW LONG THIS WHOLE PROCESS WILL TAKE
    time.sleep(3)

#check to see if we have enough marbles to dispense the correct dosage
canDispense = True
while(canDispense):
    for i in range(0, 7):
        if (totalMarbles[i] < totalDosage[i]):
            canDispense = False

    #if we have enough marbles
    if(canDispense):
        for i in range(0,7):
            if(totalDosage[i] == 0):
                continue
            else:
                for j in range(0, totalDosage[i]):
                    sorter.pop_marble_num(i)
                    totalMarbles[i] -= 1

        print('Dosage Dispensed')
        time.sleep(20)
	        #if we cannot dispense because there are not enough marbles in the sorter
    else:
        print('I do not have enough marbles to dispense this dosage: play noise')
