"""  With the Two wheels pointing forward - i.e Front Wheel Drive 

#!! Hold the L9110 this way !!

||Right Wheel    || Left Wheel    ||
|| (RED) (BLACK) || (RED) (BLACK) ||
||   Green Term Blocks  x4        ||
|| MOTOR B       ||   MOTOR A     ||
((...............PCB ..............))
((...............PCB ..............))
((...............PCB ..............))
((...............PCB ..............))
((...............PCB ..............))
| B-1A |B-1B |GND |VCC |A-1A |A-1B |  

### Truth Table

"""

import time
from machine import Pin

########## Right ##########
A1A = Pin(2, Pin.OUT)
A1B = Pin(3, Pin.OUT)

########## Left ##########
B1A = Pin(0, Pin.OUT)
B1B = Pin(1, Pin.OUT)
