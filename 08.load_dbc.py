import cantools
from can.message import Message
db = cantools.db.load_file('/home/wi/Downloads/honda.dbc')
print(db)
#dbc 파일 모두 불러오기

msg = db.get_message_by_name('WHEEL_SPEEDS')
print(msg)
#dbc 파일의 특정 부분만을 불러오기

msg_data = msg.encode({'WHEEL_SPEED_FL':100, 'WHEEL_SPEED_FR': 100, 'WHEEL_SPEED_RL': 100, 'WHEEL_SPEED_RR': 100})
print(msg_data)