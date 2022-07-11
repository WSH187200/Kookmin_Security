import cantools
from can.message import Message
import can
db = cantools.db.load_file('/home/wi/Downloads/honda.dbc')

bus = can.interface.Bus(bustype = 'socketcan', channel = 'vcan0', bitrate = 250000)


hight_delta = bytes([
        0x5A,0x6D,0x36,0x1B,0x0D,0x06,0x03,0x41,
        0x60,0x30,0x18,0x4C,0x66,0x33,0x59,0x2C,
        0x56,0x2B,0x15,0x4A,0x65,0x72,0x39,0x1C,
        0x4E,0x67,0x73,0x79,0x3C,0x5E,0x6F,0x37,
        0x5B,0x2D,0x16,0x0B,0x05,0x42,0x21,0x50,
        0x28,0x54,0x2A,0x55,0x6A,0x75,0x7A,0x7D,
        0x3E,0x5F,0x2F,0x17,0x4B,0x25,0x52,0x29,
        0x14,0x0A,0x45,0x62,0x31,0x58,0x6C,0x76,
        0x3B,0x1D,0x0E,0x47,0x63,0x71,0x78,0x7C,
        0x7E,0x7F,0x3F,0x1F,0x0F,0x07,0x43,0x61,
        0x70,0x38,0x5C,0x6E,0x77,0x7B,0x3D,0x1E,
        0x4F,0x27,0x53,0x69,0x34,0x1A,0x4D,0x26,
        0x13,0x49,0x24,0x12,0x09,0x04,0x02,0x01,
        0x40,0x20,0x10,0x08,0x44,0x22,0x11,0x48,
        0x64,0x32,0x19,0x0C,0x46,0x23,0x51,0x68,
        0x74,0x3A,0x5D,0x2E,0x57,0x6B,0x35,0x5A
        ])

hight_f0 = bytes([
        0x00,0x86,0x0D,0x8B,0x1A,0x9C,0x17,0x91,
        0x34,0xB2,0x39,0xBF,0x2E,0xA8,0x23,0xA5,
        0x68,0xEE,0x65,0xE3,0x72,0xF4,0x7F,0xF9,
        0x5C,0xDA,0x51,0xD7,0x46,0xC0,0x4B,0xCD,
        0xD0,0x56,0xDD,0x5B,0xCA,0x4C,0xC7,0x41,
        0xE4,0x62,0xE9,0x6F,0xFE,0x78,0xF3,0x75,
        0xB8,0x3E,0xB5,0x33,0xA2,0x24,0xAF,0x29,
        0x8C,0x0A,0x81,0x07,0x96,0x10,0x9B,0x1D,
        0xA1,0x27,0xAC,0x2A,0xBB,0x3D,0xB6,0x30,
        0x95,0x13,0x98,0x1E,0x8F,0x09,0x82,0x04,
        0xC9,0x4F,0xC4,0x42,0xD3,0x55,0xDE,0x58,
        0xFD,0x7B,0xF0,0x76,0xE7,0x61,0xEA,0x6C,
        0x71,0xF7,0x7C,0xFA,0x6B,0xED,0x66,0xE0,
        0x45,0xC3,0x48,0xCE,0x5F,0xD9,0x52,0xD4,
        0x19,0x9F,0x14,0x92,0x03,0x85,0x0E,0x88,
        0x2D,0xAB,0x20,0xA6,0x37,0xB1,0x3A,0xBC,
        0x43,0xC5,0x4E,0xC8,0x59,0xDF,0x54,0xD2,
        0x77,0xF1,0x7A,0xFC,0x6D,0xEB,0x60,0xE6,
        0x2B,0xAD,0x26,0xA0,0x31,0xB7,0x3C,0xBA,
        0x1F,0x99,0x12,0x94,0x05,0x83,0x08,0x8E,
        0x93,0x15,0x9E,0x18,0x89,0x0F,0x84,0x02,
        0xA7,0x21,0xAA,0x2C,0xBD,0x3B,0xB0,0x36,
        0xFB,0x7D,0xF6,0x70,0xE1,0x67,0xEC,0x6A,
        0xCF,0x49,0xC2,0x44,0xD5,0x53,0xD8,0x5E,
        0xE2,0x64,0xEF,0x69,0xF8,0x7E,0xF5,0x73,
        0xD6,0x50,0xDB,0x5D,0xCC,0x4A,0xC1,0x47,
        0x8A,0x0C,0x87,0x01,0x90,0x16,0x9D,0x1B,
        0xBE,0x38,0xB3,0x35,0xA4,0x22,0xA9,0x2F,
        0x32,0xB4,0x3F,0xB9,0x28,0xAE,0x25,0xA3,
        0x06,0x80,0x0B,0x8D,0x1C,0x9A,0x11,0x97,
        0x5A,0xDC,0x57,0xD1,0x40,0xC6,0x4D,0xCB,
        0x6E,0xE8,0x63,0xE5,0x74,0xF2,0x79,0xFF
        ])

hight_f1 = bytes([
        0x00,0x58,0xB0,0xE8,0x61,0x39,0xD1,0x89,
        0xC2,0x9A,0x72,0x2A,0xA3,0xFB,0x13,0x4B,
        0x85,0xDD,0x35,0x6D,0xE4,0xBC,0x54,0x0C,
        0x47,0x1F,0xF7,0xAF,0x26,0x7E,0x96,0xCE,
        0x0B,0x53,0xBB,0xE3,0x6A,0x32,0xDA,0x82,
        0xC9,0x91,0x79,0x21,0xA8,0xF0,0x18,0x40,
        0x8E,0xD6,0x3E,0x66,0xEF,0xB7,0x5F,0x07,
        0x4C,0x14,0xFC,0xA4,0x2D,0x75,0x9D,0xC5,
        0x16,0x4E,0xA6,0xFE,0x77,0x2F,0xC7,0x9F,
        0xD4,0x8C,0x64,0x3C,0xB5,0xED,0x05,0x5D,
        0x93,0xCB,0x23,0x7B,0xF2,0xAA,0x42,0x1A,
        0x51,0x09,0xE1,0xB9,0x30,0x68,0x80,0xD8,
        0x1D,0x45,0xAD,0xF5,0x7C,0x24,0xCC,0x94,
        0xDF,0x87,0x6F,0x37,0xBE,0xE6,0x0E,0x56,
        0x98,0xC0,0x28,0x70,0xF9,0xA1,0x49,0x11,
        0x5A,0x02,0xEA,0xB2,0x3B,0x63,0x8B,0xD3,
        0x2C,0x74,0x9C,0xC4,0x4D,0x15,0xFD,0xA5,
        0xEE,0xB6,0x5E,0x06,0x8F,0xD7,0x3F,0x67,
        0xA9,0xF1,0x19,0x41,0xC8,0x90,0x78,0x20,
        0x6B,0x33,0xDB,0x83,0x0A,0x52,0xBA,0xE2,
        0x27,0x7F,0x97,0xCF,0x46,0x1E,0xF6,0xAE,
        0xE5,0xBD,0x55,0x0D,0x84,0xDC,0x34,0x6C,
        0xA2,0xFA,0x12,0x4A,0xC3,0x9B,0x73,0x2B,
        0x60,0x38,0xD0,0x88,0x01,0x59,0xB1,0xE9,
        0x3A,0x62,0x8A,0xD2,0x5B,0x03,0xEB,0xB3,
        0xF8,0xA0,0x48,0x10,0x99,0xC1,0x29,0x71,
        0xBF,0xE7,0x0F,0x57,0xDE,0x86,0x6E,0x36,
        0x7D,0x25,0xCD,0x95,0x1C,0x44,0xAC,0xF4,
        0x31,0x69,0x81,0xD9,0x50,0x08,0xE0,0xB8,
        0xF3,0xAB,0x43,0x1B,0x92,0xCA,0x22,0x7A,
        0xB4,0xEC,0x04,0x5C,0xD5,0x8D,0x65,0x3D,
        0x76,0x2E,0xC6,0x9E,0x17,0x4F,0xA7,0xFF
        ])

key = (bytes([0x01, 0x01, 0x01, 0x01, 0x01, 0x01, 0x01, 0x01, 0x01, 0x01, 0x01, 0x01, 0x01, 0x01, 0x01, 0x01]), 
bytes([0x12, 0x12, 0x12, 0x12, 0x12, 0x12, 0x12, 0x12, 0x12, 0x12, 0x12, 0x12, 0x12, 0x12, 0x12, 0x12]), 
bytes([0x23, 0x23, 0x23, 0x23, 0x23, 0x23, 0x23, 0x23, 0x23, 0x23, 0x23, 0x23, 0x23, 0x23, 0x23, 0x23]), 
bytes([0x34, 0x34, 0x34, 0x34, 0x34, 0x34, 0x34, 0x34, 0x34, 0x34, 0x34, 0x34, 0x34, 0x34, 0x34, 0x34]), 
bytes([0x45, 0x45, 0x45, 0x45, 0x45, 0x45, 0x45, 0x45, 0x45, 0x45, 0x45, 0x45, 0x45, 0x45, 0x45, 0x45]))

def hight_key_sched(user_key, user_key_len):    
    round_key = [0] * 136
    for i in range(4):
        round_key[i] = user_key[i+12]
        round_key[i+4] = user_key[i]
    
    for i in range(8):
        for j in range(8):
            round_key[8+16*i+j] = (user_key[(j-i)&7] + hight_delta[16*i+j]) & 0xFF
        for j in range(8):
            round_key[8+16*i+j+8] = (user_key[((j-i)&7)+8] + hight_delta[16*i+j+8]) & 0xFF

    return round_key
    
def HIGHT_ENC(round_key, xx, k, i0, i1, i2, i3, i4, i5, i6, i7):
    xx[i0] = (xx[i0] ^ (hight_f0[xx[i1]] + round_key[4*k+3])) & 0xFF
    xx[i2] = (xx[i2] + (hight_f1[xx[i3]] ^ round_key[4*k+2])) & 0xFF
    xx[i4] = (xx[i4] ^ (hight_f0[xx[i5]] + round_key[4*k+1])) & 0xFF
    xx[i6] = (xx[i6] + (hight_f1[xx[i7]] ^ round_key[4*k+0])) & 0xFF    
    
def HIGHT_Encrypt(round_key, data_in, data_out):
    xx = [0] * 8
    # First Round
    xx[1] = data_in[1]
    xx[3] = data_in[3]
    xx[5] = data_in[5]
    xx[7] = data_in[7]

    xx[0] = (data_in[0] + round_key[0]) & 0xFF
    xx[2] = (data_in[2] ^ round_key[1])
    xx[4] = (data_in[4] + round_key[2]) & 0xFF
    xx[6] = (data_in[6] ^ round_key[3])

    HIGHT_ENC(round_key, xx,  2,  7,6,5,4,3,2,1,0)
    HIGHT_ENC(round_key, xx,  3,  6,5,4,3,2,1,0,7)
    HIGHT_ENC(round_key, xx,  4,  5,4,3,2,1,0,7,6)
    HIGHT_ENC(round_key, xx,  5,  4,3,2,1,0,7,6,5)
    HIGHT_ENC(round_key, xx,  6,  3,2,1,0,7,6,5,4)
    HIGHT_ENC(round_key, xx,  7,  2,1,0,7,6,5,4,3)
    HIGHT_ENC(round_key, xx,  8,  1,0,7,6,5,4,3,2)
    HIGHT_ENC(round_key, xx,  9,  0,7,6,5,4,3,2,1)
    HIGHT_ENC(round_key, xx, 10,  7,6,5,4,3,2,1,0)
    HIGHT_ENC(round_key, xx, 11,  6,5,4,3,2,1,0,7)
    HIGHT_ENC(round_key, xx, 12,  5,4,3,2,1,0,7,6)
    HIGHT_ENC(round_key, xx, 13,  4,3,2,1,0,7,6,5)
    HIGHT_ENC(round_key, xx, 14,  3,2,1,0,7,6,5,4)
    HIGHT_ENC(round_key, xx, 15,  2,1,0,7,6,5,4,3)
    HIGHT_ENC(round_key, xx, 16,  1,0,7,6,5,4,3,2)
    HIGHT_ENC(round_key, xx, 17,  0,7,6,5,4,3,2,1)
    HIGHT_ENC(round_key, xx, 18,  7,6,5,4,3,2,1,0)
    HIGHT_ENC(round_key, xx, 19,  6,5,4,3,2,1,0,7)
    HIGHT_ENC(round_key, xx, 20,  5,4,3,2,1,0,7,6)
    HIGHT_ENC(round_key, xx, 21,  4,3,2,1,0,7,6,5)
    HIGHT_ENC(round_key, xx, 22,  3,2,1,0,7,6,5,4)
    HIGHT_ENC(round_key, xx, 23,  2,1,0,7,6,5,4,3)
    HIGHT_ENC(round_key, xx, 24,  1,0,7,6,5,4,3,2)
    HIGHT_ENC(round_key, xx, 25,  0,7,6,5,4,3,2,1)
    HIGHT_ENC(round_key, xx, 26,  7,6,5,4,3,2,1,0)
    HIGHT_ENC(round_key, xx, 27,  6,5,4,3,2,1,0,7)
    HIGHT_ENC(round_key, xx, 28,  5,4,3,2,1,0,7,6)
    HIGHT_ENC(round_key, xx, 29,  4,3,2,1,0,7,6,5)
    HIGHT_ENC(round_key, xx, 30,  3,2,1,0,7,6,5,4)
    HIGHT_ENC(round_key, xx, 31,  2,1,0,7,6,5,4,3)
    HIGHT_ENC(round_key, xx, 32,  1,0,7,6,5,4,3,2)
    HIGHT_ENC(round_key, xx, 33,  0,7,6,5,4,3,2,1)

    # Final Round
    data_out[1] = xx[2] & 0xFF
    data_out[3] = xx[4] & 0xFF
    data_out[5] = xx[6] & 0xFF
    data_out[7] = xx[0] & 0xFF    

    data_out[0] = (xx[1] + round_key[4]) & 0xFF
    data_out[2] = (xx[3] ^ round_key[5]) & 0xFF
    data_out[4] = (xx[5] + round_key[6]) & 0xFF
    data_out[6] = (xx[7] ^ round_key[7]) & 0xFF



def HIGHT_DEC(round_key, xx, k, i0,i1,i2,i3,i4,i5,i6,i7):
    xx[i1] = (xx[i1] - (hight_f1[xx[i2]] ^ round_key[4*k+2])) & 0xFF
    xx[i3] = (xx[i3] ^ (hight_f0[xx[i4]] + round_key[4*k+1])) & 0xFF
    xx[i5] = (xx[i5] - (hight_f1[xx[i6]] ^ round_key[4*k+0])) & 0xFF
    xx[i7] = (xx[i7] ^ (hight_f0[xx[i0]] + round_key[4*k+3])) & 0xFF

def HIGHT_Decrypt(round_key, data_in, data_out):
    xx = [0] * 8

    xx[2] = data_in[1]
    xx[4] = data_in[3]
    xx[6] = data_in[5]
    xx[0] = data_in[7]
    
    xx[1] = (data_in[0] - round_key[4])
    xx[3] = (data_in[2] ^ round_key[5])
    xx[5] = (data_in[4] - round_key[6])
    xx[7] = (data_in[6] ^ round_key[7])
    
    HIGHT_DEC(round_key, xx, 33,  7,6,5,4,3,2,1,0)
    HIGHT_DEC(round_key, xx, 32,  0,7,6,5,4,3,2,1)
    HIGHT_DEC(round_key, xx, 31,  1,0,7,6,5,4,3,2)
    HIGHT_DEC(round_key, xx, 30,  2,1,0,7,6,5,4,3)
    HIGHT_DEC(round_key, xx, 29,  3,2,1,0,7,6,5,4)
    HIGHT_DEC(round_key, xx, 28,  4,3,2,1,0,7,6,5)
    HIGHT_DEC(round_key, xx, 27,  5,4,3,2,1,0,7,6)
    HIGHT_DEC(round_key, xx, 26,  6,5,4,3,2,1,0,7)
    HIGHT_DEC(round_key, xx, 25,  7,6,5,4,3,2,1,0)
    HIGHT_DEC(round_key, xx, 24,  0,7,6,5,4,3,2,1)
    HIGHT_DEC(round_key, xx, 23,  1,0,7,6,5,4,3,2)
    HIGHT_DEC(round_key, xx, 22,  2,1,0,7,6,5,4,3)
    HIGHT_DEC(round_key, xx, 21,  3,2,1,0,7,6,5,4)
    HIGHT_DEC(round_key, xx, 20,  4,3,2,1,0,7,6,5)
    HIGHT_DEC(round_key, xx, 19,  5,4,3,2,1,0,7,6)
    HIGHT_DEC(round_key, xx, 18,  6,5,4,3,2,1,0,7)
    HIGHT_DEC(round_key, xx, 17,  7,6,5,4,3,2,1,0)
    HIGHT_DEC(round_key, xx, 16,  0,7,6,5,4,3,2,1)
    HIGHT_DEC(round_key, xx, 15,  1,0,7,6,5,4,3,2)
    HIGHT_DEC(round_key, xx, 14,  2,1,0,7,6,5,4,3)
    HIGHT_DEC(round_key, xx, 13,  3,2,1,0,7,6,5,4)
    HIGHT_DEC(round_key, xx, 12,  4,3,2,1,0,7,6,5)
    HIGHT_DEC(round_key, xx, 11,  5,4,3,2,1,0,7,6)
    HIGHT_DEC(round_key, xx, 10,  6,5,4,3,2,1,0,7)
    HIGHT_DEC(round_key, xx,  9,  7,6,5,4,3,2,1,0)
    HIGHT_DEC(round_key, xx,  8,  0,7,6,5,4,3,2,1)
    HIGHT_DEC(round_key, xx,  7,  1,0,7,6,5,4,3,2)
    HIGHT_DEC(round_key, xx,  6,  2,1,0,7,6,5,4,3)
    HIGHT_DEC(round_key, xx,  5,  3,2,1,0,7,6,5,4)
    HIGHT_DEC(round_key, xx,  4,  4,3,2,1,0,7,6,5)
    HIGHT_DEC(round_key, xx,  3,  5,4,3,2,1,0,7,6)
    HIGHT_DEC(round_key, xx,  2,  6,5,4,3,2,1,0,7)
    
    data_out[1] = xx[1] & 0xFF
    data_out[3] = xx[3] & 0xFF
    data_out[5] = xx[5] & 0xFF
    data_out[7] = xx[7] & 0xFF
    
    data_out[0] = (xx[0] - round_key[0]) & 0xFF
    data_out[2] = (xx[2] ^ round_key[1]) & 0xFF
    data_out[4] = (xx[4] - round_key[2]) & 0xFF
    data_out[6] = (xx[6] ^ round_key[3]) & 0xFF
    
    
def print_hex(bytes_data):
    for idx, b in enumerate(bytes_data):
        print('0x%02x ' % b, end='')
        if (idx+1)%16 == 0:
            print('')
    print('')

keynum = 0

def speed_encoding(speed_value, cnt):
    if cnt%1000 == 0:
        keynum += 1
    if keynum == 5:
        keynum = 0
    round_key = hight_key_sched(key[keynum], len(key[keynum]))

    data_in = [0] * 8
    data_out = [0] * 8
    hex_data_out = [0] *8

    speed = db.get_message_by_name('WHEEL_SPEEDS')
    speed_data = speed.encode({'WHEEL_SPEED_FL':speed_value, 'WHEEL_SPEED_FR': speed_value, 'WHEEL_SPEED_RL': speed_value, 'WHEEL_SPEED_RR': speed_value})

    A = speed_data.hex()

    data_1 = A[0:2]
    data_2 = A[2:4]
    data_3 = A[4:6]
    data_4 = A[6:8]
    data_5 = A[8:10]
    data_6 = A[10:12]
    data_7 = A[12:14]
    data_8 = A[14:16]

    data_in[0] = int(data_1, 16)
    data_in[1] = int(data_2, 16)
    data_in[2] = int(data_3, 16)
    data_in[3] = int(data_4, 16)
    data_in[4] = int(data_5, 16)
    data_in[5] = int(data_6, 16)
    data_in[6] = int(data_7, 16)
    data_in[7] = int(data_8, 16)

    HIGHT_Encrypt(round_key, data_in, data_out)

    for i in range(8):
        hex_data_out[i] = hex(data_out[i])

    for i in range(8):
        if len(hex_data_out[i]) == 3:
            hex_data_out[i] = '0'+hex_data_out[i][2:3]
        else:
            hex_data_out[i] = hex_data_out[i][2:4]

    encoded_data = "".join(hex_data_out)

    speed_CAN = can.Message(arbitration_id = speed.frame_id, data = bytes.fromhex(encoded_data), is_extended_id = False)
    bus.send(speed_CAN)

def steer_encoding(steer_value, cnt):
    if cnt%1000 == 0:
        keynum += 1
    if keynum == 5:
        keynum = 0
    round_key = hight_key_sched(key[keynum], len(key[keynum]))

    data_in = [0] * 8
    data_out = [0] * 8
    hex_data_out = [0] *8

    steer = db.get_message_by_name('STEERING_SENSORS')
    steer_data = steer.encode({'STEER_ANGLE' : steer_value * 10})

    A = steer_data.hex()

    data_1 = A[0:2]
    data_2 = A[2:4]
    data_3 = A[4:6]
    data_4 = A[6:8]
    data_5 = A[8:10]
    data_6 = A[10:12]
    data_7 = A[12:14]
    data_8 = A[14:16]

    data_in[0] = int(data_1, 16)
    data_in[1] = int(data_2, 16)
    data_in[2] = int(data_3, 16)
    data_in[3] = int(data_4, 16)
    data_in[4] = int(data_5, 16)
    data_in[5] = int(data_6, 16)
    data_in[6] = int(data_7, 16)
    data_in[7] = int(data_8, 16)

    HIGHT_Encrypt(round_key, data_in, data_out)

    for i in range(8):
        hex_data_out[i] = hex(data_out[i])

    for i in range(8):
        if len(hex_data_out[i]) == 3:
            hex_data_out[i] = '0'+hex_data_out[i][2:3]
        else:
            hex_data_out[i] = hex_data_out[i][2:4]

    encoded_data = "".join(hex_data_out)

    steer_CAN = can.Message(arbitration_id = steer.frame_id, data = bytes.fromhex(encoded_data), is_extended_id = False)
    bus.send(steer_CAN)

def gear_encoding(gear_value, cnt):
    if cnt%1000 == 0:
        keynum += 1
    if keynum == 5:
        keynum = 0
    round_key = hight_key_sched(key[keynum], len(key[keynum]))

    data_in = [0] * 8
    data_out = [0] * 8
    hex_data_out = [0] *8

    gear = db.get_message_by_name('GEARBOX')

    if(gear_value == 0):
        gear_data = gear.encode({'GEAR_SHIFTER':16, 'GEAR': 19})
    elif(gear_value == -1):
        gear_data = gear.encode({'GEAR_SHIFTER':8, 'GEAR': 18})
    elif(gear_value == -2 ):
        gear_data = gear.encode({'GEAR_SHIFTER':4, 'GEAR': 17})
    else:
        gear_data = gear.encode({'GEAR_SHIFTER':32, 'GEAR': 20})

    A = gear_data.hex()

    data_1 = A[0:2]
    data_2 = A[2:4]
    data_3 = A[4:6]
    data_4 = A[6:8]
    data_5 = A[8:10]
    data_6 = A[10:12]
    data_7 = A[12:14]
    data_8 = A[14:16]

    data_in[0] = int(data_1, 16)
    data_in[1] = int(data_2, 16)
    data_in[2] = int(data_3, 16)
    data_in[3] = int(data_4, 16)
    data_in[4] = int(data_5, 16)
    data_in[5] = int(data_6, 16)
    data_in[6] = int(data_7, 16)
    data_in[7] = int(data_8, 16)

    HIGHT_Encrypt(round_key, data_in, data_out)

    for i in range(8):
        hex_data_out[i] = hex(data_out[i])

    for i in range(8):
        if len(hex_data_out[i]) == 3:
            hex_data_out[i] = '0'+hex_data_out[i][2:3]
        else:
            hex_data_out[i] = hex_data_out[i][2:4]

    encoded_data = "".join(hex_data_out)

    gear_CAN = can.Message(arbitration_id = gear.frame_id, data = bytes.fromhex(encoded_data), is_extended_id = False)
    bus.send(gear_CAN)

def brakelight_encoidng(brakelight_value, cnt):
    if cnt%1000 == 0:
        keynum += 1
    if keynum == 5:
        keynum = 0
    round_key = hight_key_sched(key[keynum], len(key[keynum]))

    data_in = [0] * 8
    data_out = [0] * 8
    hex_data_out = [0] *8

    brakelight = db.get_message_by_name('ACC_CONTROL')

    if(brakelight_value == 0):
        brakelight_data = brakelight.encode({'BRAKE_LIGHTS': 0})
    else:
        brakelight_data = brakelight.encode({'BRAKE_LIGHTS': 1})

    A = brakelight_data.hex()

    data_1 = A[0:2]
    data_2 = A[2:4]
    data_3 = A[4:6]
    data_4 = A[6:8]
    data_5 = A[8:10]
    data_6 = A[10:12]
    data_7 = A[12:14]
    data_8 = A[14:16]

    data_in[0] = int(data_1, 16)
    data_in[1] = int(data_2, 16)
    data_in[2] = int(data_3, 16)
    data_in[3] = int(data_4, 16)
    data_in[4] = int(data_5, 16)
    data_in[5] = int(data_6, 16)
    data_in[6] = int(data_7, 16)
    data_in[7] = int(data_8, 16)

    HIGHT_Encrypt(round_key, data_in, data_out)

    for i in range(8):
        hex_data_out[i] = hex(data_out[i])

    for i in range(8):
        if len(hex_data_out[i]) == 3:
            hex_data_out[i] = '0'+hex_data_out[i][2:3]
        else:
            hex_data_out[i] = hex_data_out[i][2:4]

    encoded_data = "".join(hex_data_out)

    brakelight_CAN = can.Message(arbitration_id = brakelight.frame_id, data = bytes.fromhex(encoded_data), is_extended_id = False)
    bus.send(brakelight_CAN)

def brakehold_encoding(brakehold_value, cnt):
    if cnt%1000 == 0:
        keynum += 1
    if keynum == 5:
        keynum = 0
    round_key = hight_key_sched(key[keynum], len(key[keynum]))

    data_in = [0] * 8
    data_out = [0] * 8
    hex_data_out = [0] *8

    brakehold = db.get_message_by_name('VSA_STATUS')

    if brakehold_value == True:
        brakehold_data = brakehold.encode({'BRAKE_HOLD_ACTIVE': 1, 'BRAKE_HOLD_ENABLED': 1})
    else:
        brakehold_data = brakehold.encode({'BRAKE_HOLD_ACTIVE': 0, 'BRAKE_HOLD_ENABLED': 0})

    A = brakehold_data.hex()

    data_1 = A[0:2]
    data_2 = A[2:4]
    data_3 = A[4:6]
    data_4 = A[6:8]
    data_5 = A[8:10]
    data_6 = A[10:12]
    data_7 = A[12:14]
    data_8 = A[14:16]

    data_in[0] = int(data_1, 16)
    data_in[1] = int(data_2, 16)
    data_in[2] = int(data_3, 16)
    data_in[3] = int(data_4, 16)
    data_in[4] = int(data_5, 16)
    data_in[5] = int(data_6, 16)
    data_in[6] = int(data_7, 16)
    data_in[7] = int(data_8, 16)

    HIGHT_Encrypt(round_key, data_in, data_out)

    for i in range(8):
        hex_data_out[i] = hex(data_out[i])

    for i in range(8):
        if len(hex_data_out[i]) == 3:
            hex_data_out[i] = '0'+hex_data_out[i][2:3]
        else:
            hex_data_out[i] = hex_data_out[i][2:4]

    encoded_data = "".join(hex_data_out)

    brakehold_CAN = can.Message(arbitration_id = brakehold.frame_id, data = bytes.fromhex(encoded_data), is_extended_id = False)
    bus.send(brakehold_CAN)