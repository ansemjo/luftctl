# example code for ansemjo/luftctl
# 1. flash micropython from https://micropython.org/download/esp32c3-usb/
# 2. upload with `ampy -p /dev/ttyACM0 put main.py`

from machine import Pin as pin
from time import sleep

# how long to wait between phases
wait = 5

# 12v enable
en = pin(3, pin.OUT)
en.off()

# fan pwms
f1 = pin(4, pin.OUT)
f1.off()
f2 = pin(6, pin.OUT)
f2.off()

# usr led
led = pin(10, pin.OUT)
led.off()
def blink():
  led.on()
  sleep(0.1)
  led.off()

# endless loop
while True:

  blink()
  en.on()
  sleep(wait)
  
  blink()
  f1.on()
  f2.on()
  sleep(wait)

  blink()
  en.off()
  sleep(wait)
  
  blink()
  f1.off()
  f2.off()
  sleep(wait)
