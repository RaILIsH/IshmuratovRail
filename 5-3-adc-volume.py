import RPi.GPIO as GPIO
import sys
import time as t
GPIO.setmode(GPIO.BCM)
dac = [26, 19, 13, 6, 5, 11, 9, 10]
leds = [21, 20, 16, 12, 7, 8, 25, 24]
comp = 4
troyka = 17
GPIO.setup(dac, GPIO.OUT)
GPIO.setup(leds, GPIO.OUT)
GPIO.setup(troyka, GPIO.OUT, initial = GPIO.HIGH)
GPIO.setup(comp, GPIO.IN)
def binn(a):
    return [int(i) for i in bin(a) [2:].zfill(8)]
def adc():
    k = 0
    for i in range(7, -1, -1):
        k+=2**i
        GPIO.output(dac, binn(i))
        t.sleep(0.01)
        if GPIO.input(comp) == 0:
            k-=2**i
    return k
def ans(a):
    a = int(a/256*10)
    ch = [0]*8
    for i in range(a-1):
        ch[i]=1
    return ch
try:
    while True:
        k=adc()
        GPIO.output(leds, ans(k))
finally:
    GPIO.output(dac, 0)
    GPIO.cleanup()
