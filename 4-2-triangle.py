def binn(a):
    return [int(i) for i in bin(a) [2:].zfill(8)]
import RPi.GPIO as GPIO
import sys
import time as t
dac = [26, 19, 13, 6, 5, 11, 9, 10]
GPIO.setmode(GPIO.BCM)
GPIO.setup(dac, GPIO.OUT)
try:
    while True:
        a = input()
        if not a.isdigit():
            print("vvedi chislo")
        else:
            A = int(a)/256/2
            for i in range (256):
                GPIO.output(dac, binn(i))
                t.sleep(A)
            for i in range (255, -1, -1):
                GPIO.output(dac, binn(i))
                t.sleep(A)
finally:
    GPIO.output(dac, 1)
    GPIO.cleanup