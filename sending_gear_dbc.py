import cantools
from can.message import Message
db = cantools.db.load_file('/home/wi/Downloads/honda.dbc')

gear = db.get_message_by_name('GEARBOX')
if (gear_code == 1)
gear_data = gear.encode({'GEAR_SHIFTER':100, 'GEAR': 90})

import can
bus = can.interface.Bus(bustype = 'socketcan', channel = 'vcan0', bitrate = 250000)
speed_CAN = can.Message(arbitration_id = gear.frame_id, data = gear_data, is_extended_id = False)

try:
    bus.send(speed_CAN)
    print("Message sent on {}".format(bus.channel_info))
except can.CanError:
    print("Message NOT sent")