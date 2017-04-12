#!/usr/bin/env python
from Motor import Motor
from Barcode import Barcode
from PelletIdentifier import PelletIdentifier
from Color import Color

i = 0;
totalMarbles = [0,0,0,0,0,0,0,0]
dosage = [0,0,0,0,0,0,0,0]
#read barcodes and set dosage
b = Barcode(0)
for (i < 4):
    newdosage = b.read_barcode() #change barcode functions to return dosage needed in the same form as
                    #dosage so that we can just add it to the total.
    #dosage = dosage + newdosage #may need for loop to add.
    i += 1

#identify and sort
p = PelletIdentifier(1)
while(#needs to be written: p.hasMarble()):
    color = Color(p.poll_color())
    #change function to return a number instead of a string and keep all arrays with colors in the same order.
    totalMarbles[color.identify_color()] += 1;
