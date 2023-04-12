import RPi.GPIO as GPIO
import sys
import time as t
GPIO.setmode(GPIO.BCM)
dac = [26, 19, 13, 6, 5, 11, 9, 10]
comp = 4
troyka = 17
GPIO.setup(dac, GPIO.OUT)
GPIO.setup(troyka, GPIO.OUT, initial = GPIO.LOW)
GPIO.setup(comp, GPIO.IN)
def binn(a):
    return [int (i) for i in bin(a) [2:].zfill(8)]
def adc():
    k=0
    for i in range (7, -1, -1):
        k+=2**i
        GPIO.output(dac, binn(k))
        t.sleep(0.01)
        if GPIO.input(comp)==0:
            k-=2**i
    return k
try:
    while True:
        k = adc()
        print (k*3.3/256)
finally:
    GPIO.output(dac, 0)
    GPIO.cleanup()
