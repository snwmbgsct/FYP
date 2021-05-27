
##树莓派 和  arduino串口通信调试
import serial
import time

ser = serial.Serial("/dev/ttyACM0", 115200 )



def get_humidity():
    response = ser.read_all().decode()
    
#     for i in range(3):
    while (len(response)==0):
        
        command ="start"
        ser.write(command.encode())
        time.sleep(1.1)     
        response = ser.read_all().decode()
        time.sleep(1.5) 
        if(len(response)==0):
            continue
        else:  
            humidity= response   
    return response
       

    
        

