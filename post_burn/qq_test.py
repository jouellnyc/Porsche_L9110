import time
from drive_api import CarControl

car = CarControl(speed=int(65535 * percent), freq=1000)
print(car)

time.sleep(2)
car.left_forwards()
time.sleep(2)

car.left_backwards()
time.sleep(2)

car.right_forwards()
time.sleep(2)

car.right_backwards()
time.sleep(2)

car.move_forwards()
time.sleep(2)

car.move_backwards()
time.sleep(2)

car.stop_car()
time.sleep(2)

"""
"""

car.turn_left(50)
car.debug()
time.sleep(2)

car.turn_right(50)
car.debug()
time.sleep(2)

car.turn_left(50)
car.debug()
time.sleep(2)

car.stop_car()
