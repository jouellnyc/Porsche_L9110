from machine import Pin, SoftI2C
import ssd1306

oled_width = 128
oled_height = 64

i2c = SoftI2C(scl=Pin(17), sda=Pin(16), freq=400000)
oled = ssd1306.SSD1306_I2C(oled_width, oled_height, i2c)

def first_text():
    oled.text('May the force',  0, 20)
    oled.text('Be with you...', 0, 40)
    oled.show()

first_text()

