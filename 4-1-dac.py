def binn(a):
    return [int(i) for i in bin(a)[2:].zfill(8)]
import RPi.GPIO as GPIO
import sys
dac = [26, 19, 13, 6, 5, 11, 9, 10]
GPIO.setmode(GPIO.BCM)
GPIO.setup(dac, GPIO.OUT)
try:
    while True:
        a=input()
        if a=='q':
            sys.exit()
        elif not int(a)%1==0:
            print("ne celoe")
        elif int(a)>=255:
            print("bolshe diapazona")
        elif int(a)<0:
            print("otrisatelnoe")
        else:
            GPIO.output(dac, binn(int(a)))
            print(int(a)/256*3.3)
finally:
    GPIO.output(dac, 0)
    GPIO.cleanup()
