import cantools
from can.message import Message
db = cantools.db.load_file('/home/wi/Downloads/honda.dbc')

steer = db.get_message_by_name('STEERING_SENSORS')
steer_data = steer.encode({'STEER_ANGLE': 120})

import can
bus = can.interface.Bus(bustype = 'socketcan', channel = 'vcan0', bitrate = 250000)
steer_CAN = can.Message(arbitration_id = steer.frame_id, data = steer_data, is_extended_id = False)

try:
    bus.send(steer_CAN)
    print("Message sent on {}".format(bus.channel_info))
except can.CanError:
    print("Message NOT sent")