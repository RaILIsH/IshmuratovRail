import RPi.GPIO as GPIO
import sys
import time as t
GPIO.setmode(GPIO.BCM)
GPIO.setup(2, GPIO.OUT)
dac = [26, 19, 13, 6, 5, 11, 9, 10]
pwm = GPIO.PWM(2, 1000)
pwm.start(0)
try:
    while True:
        a = int(input())
        pwm.ChangeDutyCycle(a)
        print(a*3.3/100)
finally:
    GPIO.output(2,0)
    GPIO.output(dac, 0)
    GPIO.cleanup()