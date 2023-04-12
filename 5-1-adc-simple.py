import RPi.GPIO as GPIO
import sys
import time as t
GPIO.setmode(GPIO.BCM)
dac = [26, 19, 13, 6, 5, 11, 9, 10]
comp = 4
troyka = 17
GPIO.setup(dac, GPIO.OUT)
GPIO.setup(troyka, GPIO.OUT, initial = GPIO.HIGH)
GPIO.setup(comp, GPIO.IN)
def binn(a):
    return [int (i) for i in bin(a) [2:].zfill(8)]
def adc():
    for i in range(256):
        cnt = binn(i)
        GPIO.output(dac, cnt)
        check = GPIO.input(comp)
        if check==0:
            return i
try:
    while True:
        i = adc()
        print(i/256*3.3)
finally:
    GPIO.output(dac, 0)
    GPIO.cleanup()
