import machine 
import utime 
import urandom 

pressed = False
led = machine.Pin(15,machine.Pin.OUT)
right_button = machine.Pin(16,machine.Pin.IN,machine.Pin.PULL_DOWN)
left_button = machine.Pin(14, machine.Pin.IN,machine.Pin.PULL_DOWN)
fastest_button = None 

def left_button_handler(pin):
    global pressed
    if not pressed: 
        pressed = True
        global fastest_button
        fastest_button = left_button
def right_button_handler(pin):
    global pressed
    if not pressed: 
        pressed = True
        global fastest_button
        fastest_button = right_button    

led.value(1)
utime.sleep(urandom.uniform(5,10))
led.value(0)
timer_start = utime.ticks_ms()
left_button.irq(trigger=machine.Pin.IRQ_RISING, handler=left_button_handler)
right_button.irq(trigger=machine.Pin.IRQ_RISING, handler=right_button_handler)
while fastest_button is None: 
    utime.sleep(1)

if fastest_button is left_button:
    print("Left Player wins!")
elif fastest_button is right_button:
    print("Right Player wins!")
else: 
    print("Unable to read pin")
    print("Pin read out is: {}".format(fastest_button))
    