from machine import Pin, PWM
from utime import sleep
from tm1637 import TM1637

led = Pin(25,Pin.OUT)

dirPin = Pin(0,Pin.OUT)
stepPin = Pin(1)

slpPin = Pin(2,Pin.IN,Pin.PULL_UP) # 右
incPin = Pin(3,Pin.IN,Pin.PULL_UP) # 上
decPin = Pin(4,Pin.IN,Pin.PULL_UP) # 下
nonPin = Pin(5,Pin.IN,Pin.PULL_UP) # 左

tmClkPin=Pin(27,Pin.IN)
tmDioPin=Pin(28,Pin.IN)

rotateForMin = 60
isActive = True

def toggle(pin):
    global isActive
    led.value(not led.value())
    if isActive:
        pwm.deinit()
    else:
        pwm.init(freq=freq,duty_u16=DUTY_50)
    isActive = not isActive

def increment(pin):
    global rotateForMin
    led.value(not led.value())
    if rotateForMin>=120:return
    rotateForMin = rotateForMin +1
    tm.number(rotateForMin)

def decrement(pin):
    global rotateForMin
    led.value(not led.value())
    if rotateForMin<=60:return
    rotateForMin = rotateForMin -1
    tm.number(rotateForMin)  


Pin.irq(slpPin, trigger=Pin.IRQ_FALLING, handler=toggle)
Pin.irq(incPin, trigger=Pin.IRQ_FALLING, handler=increment)
Pin.irq(decPin, trigger=Pin.IRQ_FALLING, handler=decrement)


# ステッピングモータの設定
STEPS = 200  # 1回転に必要なステップ数
DUTY_50 = int(2**16/2)
freq = int(rotateForMin/60*STEPS*2)

dirPin.on()
pwm = PWM(stepPin,freq=freq,duty_u16=DUTY_50)


tm=TM1637(clk=tmClkPin,dio=tmDioPin)
tm.number(rotateForMin)

