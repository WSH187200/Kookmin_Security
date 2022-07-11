import can

bus = can.interface.Bus(bustype = 'socketcan', channel = 'vcan0', bitrate = 250000)
msg = can.Message(arbitration_id = 0x00, data = [10, 10, 10, 10, 10, 10, 10, 10], is_extended_id = False)
try:
    bus.send_periodic(msg, 0.01)
    print("Message sent on {}".format(bus.channel_info))
    while True:
      message = bus.recv()
      print(message)

except can.CanError:
    print("Message NOT sent")


