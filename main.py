from drive_claude_api import CarControl
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


