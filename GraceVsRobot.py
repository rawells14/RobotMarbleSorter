import time
from Motor import Motor
from Barcode import Barcode
from Sorter import Sorter
from PelletIdentifier import PelletIdentifier
from Color import Color

#sorter order: [Steel, HDPE, small white, large white, small blue, large blue,
# small red, large red]


#ROBOT SETUP INSTRUCTIONS:
#Barcode Motor in port A when robot booted
#Sorter conveyer belt in port B when robot booted
#Sorter popper servo in port C when robot booted
#Barcode Sensor in port 1 when robot booted
#Pellet Sensor in port 2 when robot booted
#
#DO NOT UNPLUG OR MOVE ANYTHING.
#IF YOU DO, RESET EVERYTHING AS IN THE INSTRUCTIONS THEN REBOOT

#to be added to when marble is sorted into bin in sorter order
totalMarbles = [0,0,0,0,0,0,0,0]
#to be added to when barcode is read in sorter order
totalDosage = [0,0,0,0,0,0,0,0]

barcodeReader = Barcode(0,0)
pelletReader = PelletIdentifier(1)
sorter = Sorter(1, 2)

#read in 4 barcodes and store the dosages from each
dosagesToAdd = []
for i in [0,1,2,3]:
    dosagesToAdd.append(barcodeReader.process_code_dosage(barcodeReader.read_barcode()))

#add dosages from barcodes to the total dosage that will be dispensed at the end
for i in [0,1,2,3]:
    totalDosage[dosagesToAdd[i][0][0]] += dosagesToAdd[i][0][1]
    totalDosage[dosagesToAdd[i][1][0]] += dosagesToAdd[i][1][1]

#start sorting process
#wait until there is a marble to read
while (!pelletReader.isMarble()):


#once marble is found continue reading marbles until the box is seen again
while(!pelletReader.isMarble()):
    marbleNum = -1
    marbleNum = pelletReader.identify()
    #if it was not in any range, continue and read again
    if (marbleNum < 0):
        continue
    #if it was trash, set it equal to 8 so that the sorter will move to trash position
    elif(marbleNum > 7):
        marbleNum = 8
    #if it was an actual marble, add to the total number of marbles of that type
    else:
        totalMarbles[i] += 1
    sorter.move_to_marble_num(marbleNum)

    #NEED TO PLAY WITH THIS NUMBER BECAUSE TIMING OF PISTON WILL BE CONSTANT AND IDK
    #HOW LONG THIS WHOLE PROCESS WILL TAKE
    time.sleep(4)

#now we dispense

#check to see if we have enough marbles to dispense the correct dosage
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
    #figure out how to actually play noise
    print('play noise')
