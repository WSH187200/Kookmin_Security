import cantools
from can.message import Message
db = cantools.db.load_file('/home/wi/Downloads/honda.dbc')

msg = db.get_message_by_name('WHEEL_SPEEDS')
msg_data = msg.encode({'WHEEL_SPEED_FL':100, 'WHEEL_SPEED_FR': 100, 'WHEEL_SPEED_RL': 100, 'WHEEL_SPEED_RR': 100})

import can
bus = can.interface.Bus(bustype = 'socketcan', channel = 'vcan0', bitrate = 250000)
msg = can.Message(arbitration_id = msg.frame_id, data = msg_data, is_extended_id = False)

try:
    bus.send(msg)
    print("Message sent on {}".format(bus.channel_info))
except can.CanError:
    print("Message NOT sent")


