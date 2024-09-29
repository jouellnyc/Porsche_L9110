import time
from drive_api import CarControl

percent=1
car = CarControl(speed=int(65535 * percent), freq=1000)

#The 'OK' Button and 1, 2, 3
pri_scan_codes=[28, 69, 70, 71, 64, 68]

def infrared_check(data):
    if data in pri_scan_codes:
        print('OK', data)
        if data == 69:
            car.stop()
            car.move_forward()
        elif data == 70:
            car.stop()
            car.move_backward()
        elif data == 64:
            car.turn_right(50)
        elif data == 68:
            car.turn_left(50)
        elif data == 71:
            car.stop()
            car.turn_left(50)
            time.sleep(5)
            car.turn_right(50) 
        elif data == 28:
            car.stop()
    else:
        print('Not in pri_scan_codes', data)
                           
                