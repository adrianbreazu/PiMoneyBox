import RPi.GPIO as GPIO

GPIO_PIN = 4

class Servo:
    def __init__(self):
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(GPIO_PIN, GPIO.OUT)
        pwm = GPIO.PWM(4, 100)
        pwm.start(1)
    
    def __update_angle__ (self, angle):
        new_angle = float(angle) / 10.0 + 2.5
        pwm.ChangeDutyCycle(new_angle)        


    def open(self):
        __update_angle__(90)
        __close_gpio__()


    def __close_gpio__(self):
        pwm.stop()
        GPIO.cleanup()