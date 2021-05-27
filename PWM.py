import RPi.GPIO as GPIO
import time

pwm_pin = 18
AIN2 = 14
AIN1 =15

GPIO.setmode(GPIO.BCM)
GPIO.setup(pwm_pin,GPIO.OUT)
GPIO.setup(AIN2,GPIO.OUT)
GPIO.setup(AIN1,GPIO.OUT)
pwm = GPIO.PWM(pwm_pin,320)
GPIO.setwarnings(False) 

def motorspeed(speed):
    if(speed>=0):
        GPIO.output(AIN1,GPIO.LOW)
        GPIO.output(AIN2,GPIO.HIGH)
        pwm.start(speed)
        time.sleep(0.02)
    else:
        GPIO.output(AIN1,GPIO.HIGH)
        GPIO.output(AIN2,GPIO.LOW)
        pwm.start(-speed)
        time.sleep(0.02)

def motorstop():
    GPIO.output(AIN1,GPIO.LOW)
    GPIO.output(AIN2,GPIO.LOW)


 
# motorspeed(50)
# time.sleep(20)
# motorspeed(-20)
# time.sleep(3)
# motorstop()
# 
# pwm.stop()
# GPIO.cleanup()