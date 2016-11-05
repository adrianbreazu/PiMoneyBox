import RPi.GPIO as GPIO

GPIO_PIN = 4

class Servo:
    def __init__(self):
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(GPIO_PIN, GPIO.OUT)
        pwm = GPIO.PWM(4, 100)
        pwm.start(1)
    
    def __update_angle__ (self, angle):
        pwm.ChangeDutyCycle(angle)        


    def open(self):
        # keep close
        self.__update_angle__(2.5)
        # open
        self.__update_angle__(4)
        self.__close_gpio__()


    def __close_gpio__(self):
        pwm.stop()
        GPIO.cleanup()