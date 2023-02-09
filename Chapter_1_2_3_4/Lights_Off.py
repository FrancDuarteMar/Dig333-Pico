import machine

led_onboard = machine.Pin("LED",  machine.Pin.OUT) #For onboard LED 
led_red = machine.Pin(15, machine.Pin.OUT)
led_yellow = machine.Pin(14,machine.Pin.OUT)
led_green = machine.Pin(13,machine.Pin.OUT)

led_red.value(0)
led_yellow.value(0)
led_green.value(0)
led_onboard.value(0)
