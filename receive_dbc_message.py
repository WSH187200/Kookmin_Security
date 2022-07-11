import cantools
from can.message import Message
db = cantools.db.load_file('/home/wi/Downloads/honda.dbc')

import can
bus = can.interface.Bus(bustype = 'socketcan', channel = 'vcan0', bitrate = 250000)
while True:
    message = bus.recv()
    print(db.decode_message(message.arbitration_id, message.data))