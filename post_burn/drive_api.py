import time
from machine import Pin, PWM
from wheels import A1A, A1B, B1A, B1B 

class CarControl:
    def __init__(self, speed=65535, freq=1000):
        """ init """
        self.A1A = A1A
        self.A1B = A1B
        self.B1A = B1A
        self.B1B = B1B

        """ PWM """
        self.Lforward  = PWM(self.A1A, freq=freq, duty_u16=0)
        self.Lbackward = PWM(self.A1B, freq=freq, duty_u16=0)
        self.Rforward  = PWM(self.B1A, freq=freq, duty_u16=0)
        self.Rbackward = PWM(self.B1B, freq=freq, duty_u16=0)
        
        """  Initial speed (0-65535) """
        self.speed       = speed
        self.left_speed  = speed
        self.right_speed = speed
        # If the wheel does not get this minimum, it just does not move well and get's stuck 
        self.minimum_turn_speed_per_wheel = 45535
    
    def move_forwards(self):
        self.right_forwards()
        self.left_forwards()
    
    def move_backwards(self):
        self.right_backwards()
        self.left_backwards()
    
    def right_forwards(self):
        self.Rforward.duty_u16(65535)
        self.Rbackward.duty_u16(0)
    
    def right_backwards(self):
        self.Rforward.duty_u16(0)
        self.Rbackward.duty_u16(65535)
        
    def left_forwards(self):
        self.Lforward.duty_u16(65535)
        self.Lbackward.duty_u16(0)
    
    def left_backwards(self):
        self.Lforward.duty_u16(0)
        self.Lbackward.duty_u16(65535)
        
    def stop_car(self):
        """Move the car forward"""
        self.Rforward.duty_u16(0)
        self.Rbackward.duty_u16(0)
        self.Lforward.duty_u16(0)
        self.Lbackward.duty_u16(0)
        
    def turn_right(self, turn_rate):
        """
        Turn right by reducing the right wheel speed
        turn_rate: 0-100 (percentage to reduce right wheel speed)
        """
        self.left_speed   = self.speed
        self.Lforward.duty_u16(self.left_speed)
        
        self.right_speed = max(self.minimum_turn_speed_per_wheel, int(self.speed * ((100 - turn_rate) / 100)))
        self.Rforward.duty_u16(self.right_speed)
    
    def turn_left(self, turn_rate):
        """
        Turn left by reducing the left wheel speed
        turn_rate: 0-100 (percentage to reduce right wheel speed)
        """
        self.right_speed   = self.speed
        self.Rforward.duty_u16(self.left_speed)
        
        self.left_speed = max(self.minimum_turn_speed_per_wheel, int(self.speed * ((100 - turn_rate) / 100)))
        self.Lforward.duty_u16(self.left_speed)
    
    def debug(self):
        print("LF ", self.Lforward.duty_u16())
        print("RF ", self.Rforward.duty_u16())
        print("RB ", self.Rbackward.duty_u16())
        print("LB ", self.Lbackward.duty_u16())
        
    def __repr__(self):
        return (f"B1A={self.B1A}, B1B={self.B1B}, B1A={self.B1A}, B1B={self.B1B}")   

