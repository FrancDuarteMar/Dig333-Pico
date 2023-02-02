import machine
# import time
import utime

led_onboard = machine.Pin("LED",  machine.Pin.OUT) #For onboard LED 
# led_external = machine.Pin(15, machine.Pin.OUT)

# led_onboard.value(1)
# utime.sleep(5)
# led_onboard.value(0)

while True:
    led_onboard.toggle()
    # led_external.toggle()
    utime.sleep(3)


