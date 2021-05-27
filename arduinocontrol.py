import time
import datetime
import query
import API_Final as API
import pos_pid
import fuzzycontrol
import PWM
import communication



opt_humi = 0.5*(query.SRAH_min+query.SRAH_max)



def  Humifuzzy(error,ec):
    if error<=0 :
        return 0
    else:       
        return fuzzycontrol.fuzzyctrl(error, ec)
                 

def main(m=0):
    print("Start collection data,interval [%s] minutes" %(m));
    while True:
        while True:
            now=datetime.datetime.now()
            if now.minute % m == 0:
#                 PWM.pwm.stop()
#                 PWM.GPIO.cleanup()
                break
            
            time.sleep(20)
            
        print(datetime.datetime.now())
        print("\n")
        
        humi_last = float(communication.get_humidity())
        time.sleep(1)
        print("humi_last=",humi_last)
        
        
      
        dhumi = opt_humi-float(communication.get_humidity())
        hc = float(communication.get_humidity())-humi_last
        print("hc=",hc)
        pwm_speed=Humifuzzy(dhumi,hc)
        
        print("speed = ",pwm_speed)
        PWM.motorspeed(pwm_speed)
                
        
     
    
        
        if m>1:
            time.sleep((m-1)*60)
        
        else:
            time.sleep(3)
              
main(1)
