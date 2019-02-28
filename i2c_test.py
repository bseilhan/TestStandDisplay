from smbus import SMBus
import time
import struct 

bus = SMBus(1)

# This is the address we setup in the Arduino Program
SLAVE_ADDRESS = 0x04

def get_data():
    return bus.read_i2c_block_data(SLAVE_ADDRESS,0,4)

def get_float(data, index=0):
    bytes = bytearray(data[4*index:(index+1)*4])
    print(data)
    return struct.unpack("f", bytes)[0]


def writeNumber(value):
    bus.write_byte_data(SLAVE_ADDRESS, 0, value)
    return -1

def readNumber():
    data = get_data()
    number = get_float(data,0)
    return number

while True:
    writeNumber(6)
    
    number = readNumber()
    print(number)
    time.sleep(0.5)