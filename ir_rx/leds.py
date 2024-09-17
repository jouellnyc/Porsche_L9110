import machine

grn  = machine.Pin(18, machine.Pin.OUT)
yll  = machine.Pin(19, machine.Pin.OUT)
red  = machine.Pin(20, machine.Pin.OUT)

grn2  = machine.Pin(28, machine.Pin.OUT)
yll2  = machine.Pin(26, machine.Pin.OUT)
red2  = machine.Pin(21, machine.Pin.OUT)


def all_off():
    for x in [grn, grn2, yll, yll2, red, red2]:
        x.off()