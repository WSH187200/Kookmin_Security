import can

bus = can.interface.Bus(bustype = 'socketcan', channel = 'vcan0', bitrate = 250000)
msg = can.Message(arbitration_id = 0x01, data = [0, 10, 0, 1, 3, 1, 4, 1], is_extended_id = False)
try:
    bus.send(msg)
    print("Message sent on {}".format(bus.channel_info))
except can.CanError:
    print("Message NOT sent")


    