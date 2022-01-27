# example code for ansemjo/luftctl
# 1. flash micropython from https://micropython.org/download/esp32c3-usb/
# 2. upload with `ampy -p /dev/ttyACM0 put main.py`

from machine import Pin as pin
from time import sleep, ticks_ms as ticks, ticks_diff as diff

# 12v enable
en = pin(3, pin.OUT)
en.off()

# fan pwms
f1 = pin(4, pin.OUT)
f1.off()
f2 = pin(6, pin.OUT)
f2.off()

# button
btn = pin(9, pin.IN)

# usr led
led = pin(10, pin.OUT)
led.off()
def blink():
  led.on()
  sleep(0.1)
  led.off()


# states to cycle through
states = [
  lambda: (blink(), en.off(), f1.off(), f2.off()),
  lambda: (blink(), en.off(), f1.on(), f2.on()),
  lambda: (blink(), en.on(), f1.off(), f2.off()),
  lambda: (blink(), en.on(), f1.on(), f2.on()),
]

# button callback for state change
i = 0
now = ticks()
def nextstate(_):
  global i, now
  if diff(ticks(), now) < 300:
    print("debounce")
    return
  now = ticks()
  i = (i+1) % len(states)
  print(f"next: {i+1}/{len(states)}")
  states[i]()

# register callback on falling edge / button press
btn.irq(trigger=pin.IRQ_FALLING, handler=nextstate)
