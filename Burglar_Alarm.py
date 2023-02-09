import machine 
import utime 

sensor_pir = machine.Pin(28,machine.Pin.IN, machine.Pin.PULL_DOWN)
analog_value = machine.ADC(28)
led = machine.Pin(15,machine.Pin.OUT)
alarm_threshold = 42000
buzzer = machine.Pin(14,machine.Pin.OUT)

while True:
    print(analog_value.read_u16())
    led.toggle()
    utime.sleep(5)
    if(analog_value.read_u16() > alarm_threshold):
        print(analog_value.read_u16())

        print("Alarm! Motion detected!")
        for i in range(50):
            led.toggle()
            buzzer.toggle()
            utime.sleep_ms(100)
    
# def pir_handler(pin):
#     utime.sleep_ms(100)
#     if(analog_value.read_u16() >0):
#         print("Alarm! Motion detected!")
#         for i in range(50):
#             led.toggle
#             utime.sleep_ms(100)
        
# sensor_pir.irq(trigger=machine.Pin.IRQ_RISING, handler=pir_handler)



