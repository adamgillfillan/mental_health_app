'''
Created on Mar 30, 2014

@author: cyborg
'''

import serial
import re
from socket import *
import requests as r

udp_ip = "http://localhost"
udp_port = 8000
udp_route = "/mental/addvoltages/"




ser = serial.Serial('/dev/ttyACM2', 9600)

while (True):
    data_array = {"voltages":[]}
    data = ser.readline()
    data = data.decode("utf-8")
    data = int(re.match(r'\d+', data).group())
    data_array["voltages"].append(data)
    response = r.post(udp_ip + ":" + str(udp_port) + udp_route, data = data_array)
    response.raise_for_status()
    
    #data = data[:4]
    print(data)
    
    