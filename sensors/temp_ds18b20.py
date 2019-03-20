#########################################
#    Configurations
sensor_serial = '28-02199245b4f5' # serial number of DS18B20
time_interval = 1 # time interval between temprature readings in seconds

#########################################

import os
import time

# load drivers
os.system('modprobe w1-gpio')
os.system('modprobe w1-therm')

temp_sensor = '/sys/bus/w1/devices/' + sensor_serial + '/w1_slave'

def temp_raw():
    f = open(temp_sensor, 'r')
    lines = f.readlines()
    f.close()
    return lines

def read_temp():
    lines = temp_raw()
    while lines[0].strip()[-3:] != 'YES':
    # wait and retry until probe reports positive readings
        time.sleep(0.2)
        lines = temp_raw()
    # valid readings received
    temp_output = lines[1].find('t=')
    if temp_output != -1:
        temp_string = lines[1].strip()[temp_output+2:]
        temp_c = float(temp_string) / 1000.0
        return str(temp_c)

while True:
    print(str(time.time())+" "+read_temp()+' centigrade')
    time.sleep(time_interval)



# EOF
