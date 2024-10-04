###LEFT

#Backwards
from machine import Pin, PWM
pinl1 = Pin(2, Pin.OUT)
pinl2 = Pin(3, Pin.OUT)
pinl1.value(1)
pinl2.value(0)
pinlpwml = Pin(14, Pin.OUT)
L =  PWM(pinlpwml, freq=1000)
#L.duty_u16(65535)


#Forwards
from machine import Pin, PWM
pinl1 = Pin(2, Pin.OUT)
pinl2 = Pin(3, Pin.OUT)
pinl1.value(0) 
pinl2.value(1)
pinlpwml = Pin(14, Pin.OUT)
L =  PWM(pinlpwml, freq=1000)
#L.duty_u16(65535)

###RIGHT
#Backwards
from machine import Pin, PWM
pinl3 = Pin(0, Pin.OUT)
pinl4 = Pin(1, Pin.OUT)
pinl3.value(1)
pinl4.value(0)
pinlpwmr = Pin(15, Pin.OUT)
R =  PWM(pinlpwmr, freq=1000)
#L.duty_u16(65535)


#Forwards
from machine import Pin, PWM
pinl3 = Pin(0, Pin.OUT)
pinl4 = Pin(1, Pin.OUT)
pinl3.value(0)
pinl4.value(1)
pinlpwmr = Pin(15, Pin.OUT)
R =  PWM(pinlpwmr, freq=1000)
#L.duty_u16(65535)
