import time
from machine import Pin, PWM

from wheels import LEFT_B_B1A, LEFT_B_B1B, RIGHT_B_B1A, RIGHT_B_B1B

""" Examples
from drive_api import CarControl
import time

percent=1
car = CarControl(speed=int(65535 * percent), freq=1000)

car.move_forward()
time.sleep(2)
car.stop()

car.move_backward()
time.sleep(2)
car.stop()

car.turn_left(50)  # Turn left, reducing left wheel to 50% of current speed
time.sleep(2)
car.stop()

car.turn_right(50)  # Turn right, reducing right wheel to 25% of current speed
time.sleep(2)
car.stop()

"""


class CarControl:
    def __init__(self, speed=65535, freq=1000):
        
        # Left wheel setup 
        self.LEFT_B_B1A = LEFT_B_B1A
        self.LEFT_B_B1A.value(0)
        
        self.LEFT_B_B1B = LEFT_B_B1B
        self.LEFT_B_B1B.value(0)
        
        # Right wheel setup
        self.RIGHT_B_B1A = RIGHT_B_B1A
        self.RIGHT_B_B1A.value(0)
        
        self.RIGHT_B_B1B = RIGHT_B_B1B
        self.RIGHT_B_B1B.value(0)
        
        # PWM setup
        self.Lforward  = PWM(self.LEFT_B_B1B, freq=freq)
        self.Lbackward = PWM(self.LEFT_B_B1A, freq=freq)
        
        self.Rforward  = PWM(self.RIGHT_B_B1B, freq=freq)
        self.Rbackward = PWM(self.RIGHT_B_B1A, freq=freq)
        
        # Initial speed (0-65535)
        self.speed = speed
    
    def stop_back_wheels(self):
        self.Lbackward.duty_u16(0)
        self.Rbackward.duty_u16(0)
        
    def stop_front_wheels(self):
        self.Lforward.duty_u16(0)
        self.Rforward.duty_u16(0)
        
    def move_forward(self):
        """Move the car forward"""
        self.stop_back_wheels()
        self.Lforward.duty_u16(self.speed)
        self.Rforward.duty_u16(self.speed)
        
    def move_backward(self):
        """Move the car backward"""
        self.stop_front_wheels()
        self.Lbackward.duty_u16(self.speed)
        self.Rbackward.duty_u16(self.speed)
        
    def stop(self):
        """Stop the car"""
        self.stop_front_wheels()
        self.stop_back_wheels()
        
    def turn_left(self, turn_rate):
        """
        Turn left by reducing the left wheel speed
        turn_rate: 0-100 (percentage to reduce), max to 50%
        ###jjo don't let it slip below 50
        """
        self.left_speed = max(45535, int(self.speed * ((100 - turn_rate) / 100)))
        self.right_speed   = self.speed
        
        self.Rforward.duty_u16(self.right_speed)
        self.Lforward.duty_u16(self.left_speed)
        
        self.stop_back_wheels()
        print("LS, RS", self.left_speed, self.right_speed)
        
    def turn_right(self, turn_rate):
        """
        Turn right by reducing the right wheel speed
        turn_rate: 0-100 (percentage to reduce right wheel speed)
        """
        self.right_speed = max(45535, int(self.speed * ((100 - turn_rate) / 100)))
        self.left_speed   = self.speed
        
        self.Rforward.duty_u16(self.right_speed)
        self.Lforward.duty_u16(self.left_speed)
        self.stop_back_wheels()
        
        print("LS, RS", self.left_speed, self.right_speed)        
    
    