import machine
import utime
import _thread

led_red = machine.Pin(15, machine.Pin.OUT)
led_yellow = machine.Pin(14,machine.Pin.OUT)
led_green = machine.Pin(13,machine.Pin.OUT)


button = machine.Pin(16, machine.Pin.IN, machine.
                     Pin.PULL_DOWN)
buzzer = machine.Pin(12, machine.Pin.OUT)

global button_pressed
button_pressed = False

def button_reader_thread():
    global button_pressed
    while True:
        if  machine.Pin(16, machine.Pin.IN, machine.
                     Pin.PULL_DOWN).value()== 1:
            button_pressed = True
            
_thread.start_new_thread(button_reader_thread,())

while True:
    if button_pressed == True:
        led_red.value(1)
        for i in range(10):
            buzzer.value(1)
            utime.sleep(0.2)
            buzzer.value(0)
            utime.sleep(0.2)
        global button_pressed
        button_pressed = 0
        
    led_red.value(0)       
    led_red.toggle()
    utime.sleep(2)
    led_red.toggle()
    led_yellow.toggle()
    utime.sleep(1)
    led_yellow.toggle()
    led_green.toggle()
    utime.sleep(4)
    led_green.toggle()

    
