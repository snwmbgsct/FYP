
import time
import datetime
import query
import fuzzycontrol
import PWM
import bme
import RPi.GPIO as GPIO
GPIO.setwarnings(False)

temperature,pressure,humidity = bme.readBME280All()

opt_temp = 0.5*(query.Tgr_max+query.Tgr_min)

opt_humi = 0.5*(query.SRAH_min+query.SRAH_max)

def  Humifuzzy(error,ec):
    if error<=-8 :
        return 0
    else:       
        return fuzzycontrol.fuzzyctrl(error, ec)
    

def main(m=0):
    while True:
        while True:
            now=datetime.datetime.now()
            if now.minute % m == 0:
                break
            time.sleep(20)
        print(datetime.datetime.now())
        temperature,pressure,humidity = bme.readBME280All()
        humi_last =humidity
        temperature,pressure,humidity = bme.readBME280All()
        dhumi =humidity - opt_humi
        dhumi_max = 100 - opt_humi
        dhumi_norm =100*(dhumi/dhumi_max)
        hc = 100*(humidity - humi_last)
        pwm_speed=Humifuzzy(dhumi_norm,hc)
        PWM.motorspeed(pwm_speed)
        if m>1:
            time.sleep((m-1)*60)
        else:
            time.sleep(3)
try:
    main(1)
except:
    GPIO.PWM(pwm_pin,320).stop()
    GPIO.cleanup()
GPIO.cleanup()