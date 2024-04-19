from machine import Pin
from utime import sleep

led = Pin(25,Pin.OUT)

for i in range(5):
    led.value(not led.value())
    sleep(0.5)
