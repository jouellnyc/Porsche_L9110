from machine import Pin, PWM
import time

""" Naming Convention: SIDE_CONTROLLER_PINNAME        """
""" We are using the B Side controller for both sides """
        
""" LEFT FRONT WHEEL """
LEFT_B_B1A = Pin(1, Pin.OUT)
LEFT_B_B1B = Pin(0, Pin.OUT)
LEFT_A_A1A = None
LEFT_A_A1B = None

""" RIGHT FRONT WHEEL """
RIGHT_B_B1A = Pin(14, Pin.OUT)
RIGHT_B_B1B = Pin(15, Pin.OUT)
RIGHT_A_A1A = None
RIGHT_A_A1B = None
