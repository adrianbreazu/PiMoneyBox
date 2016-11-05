import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(4, GPIO.OUT)
pwm = GPIO.PWM(4, 100)
pwm.start(7.5)

class Test:
    def Update_angle (self, angle):
        pwm.ChangeDutyCycle(angle)        


if __name__ == "__main__":
    test = Test()
    # move to 0
    test.Update_angle(7.5)
    time.sleep(5)
    # move to 90
    test.Update_angle(2.5)
    time.sleep(5)
    # move to -90
    test.Update_angle(12.5)
    time.sleep(5)
    pwm.stop()    
    GPIO.cleanup()