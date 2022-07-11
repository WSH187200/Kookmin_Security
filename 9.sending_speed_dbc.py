import cantools
from can.message import Message
db = cantools.db.load_file('/home/wi/Downloads/honda.dbc')

speed = db.get_message_by_name('WHEEL_SPEEDS')
speed_data = speed.encode({'WHEEL_SPEED_FL':100, 'WHEEL_SPEED_FR': 100, 'WHEEL_SPEED_RL': 100, 'WHEEL_SPEED_RR': 100},'utf-8')

speed_d_data = speed_data.hex()

import can
bus = can.interface.Bus(bustype = 'socketcan', channel = 'vcan0', bitrate = 250000)
speed_CAN = can.Message(arbitration_id = speed.frame_id, data = speed_data, is_extended_id = False)



try:
    bus.send(speed_CAN)
    print("Message sent on {}".format(bus.channel_info))
except can.CanError:
    print("Message NOT sent")
