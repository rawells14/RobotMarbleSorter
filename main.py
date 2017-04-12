#!/usr/bin/env python
import time
from Motor import Motor
from Barcode import Barcode
#motor = Motor(2)
b = Barcode(1, 0)
b.read_barcode()
