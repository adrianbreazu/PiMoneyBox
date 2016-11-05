import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(4, GPIO.OUT)
pwm = GPIO.PWM(4, 100)
pwm.start(2.5)

def change(k):
    pwm.ChangeDutyCycle(k)
    time.sleep(1)

try:
    while True:
        k = float(raw_input("enter angle: "))
        k = (1+(float(k)/180))/20
        change(k)

except KeyboardInterrupt:
    pwm.stop()
    GPIO.cleanup()
    exit