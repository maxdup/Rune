import struct


with open('db.rune', 'wb') as f:
    f.write(struct.pack('i', 256))