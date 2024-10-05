import time
from drive_api import CarControl

percent=1 #1, .9, .8, etc.
car = CarControl(speed=int(65535 * percent), freq=1000)
print(car)

#The 'OK' Button and 1, 2, 3
pri_scan_codes=[28, 69, 70, 71, 64, 68]

DEBUG=True
def debug():
    if DEBUG:
        car.debug()
        
def infrared_check(data):
    if data in pri_scan_codes:
        print('OK', data)
        if data == 69:                #1
            car.move_forwards()
            debug()
        elif data == 70:              #2
            car.move_backwards()
            debug()
        elif data == 68:              #4
            car.turn_left(7.5)
            debug()
        elif data == 64:              #5
            car.turn_right(7.5)
            debug()
        elif data == 71:
            car.turn_left(7.5)
            debug()
            time.sleep(5)
            car.turn_right(7.5)
            debug()
        elif data == 28:               #OK 
            car.stop_car()
            debug()
    else:
        print('Not in pri_scan_codes', data)
                           
                