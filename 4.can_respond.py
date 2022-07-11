import can

bus = can.interface.Bus(bustype = 'socketcan', channel = 'vcan0', bitrate = 250000)
try:
    while True:
      message = bus.recv()
      print(message.arbitration_id)

      if message.arbitration_id == 1:
          msg = can.Message(arbitration_id = 0x02, data = [0, 10, 0, 1, 3, 1, 4, 1], is_extended_id = False)
          bus.send(msg)

except can.CanError:
    print("Message NOT sent")

    