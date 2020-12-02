from grovepi import *
import time

def version():
    write_i2c_block(address, version_cmd + [unused, unused, unused])
    time.sleep(.1)
    read_i2c_byte(address)
    number = read_i2c_block(address)
    return "%s.%s.%s" % (number[1], number[2], number[3])

print(version())