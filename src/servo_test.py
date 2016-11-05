import time
import RPi.GPIO as GPIO

GPIO.setmode (GPIO.BCM)
GPIO.setup(4, GPIO.OUT)
pwm = GPIO.PWM(4, 100)
pwm.start(5)

class Test:
    def Update_angle (self, angle):
        new_angle = float(angle) / 10.0 + 2.5
        pwm.ChangeDutyCycle(new_angle)


if __name__ == "__main__":
    test = Test()
    test.Update_angle(150)
