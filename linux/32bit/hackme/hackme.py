
import ctypes
import numpy as np

libs = ctypes.CDLL('libc.so.6')

byte_804869C = [0x6A, 0xFB, 0x4C, 0x8D, 0x58, 0x0F,
                0xD4, 0xE8, 0x94, 0x98, 0xEE, 0x6B,
                0x18, 0x30, 0xE0, 0x55, 0xC5, 0x28,
                0x0E, 0x90]

v10 = ['.'] * 19

for i in range(10):
    v3 = libs.random() % 19
    v4 = 0
    v5 = byte_804869C[v3]
    v9 = v3 + 1
    v7 = 0
    # print(v7, v9)
    # while True:
    while True:
        v7 += 1
        if v7 > v9:
            break
        v4 = 1828812941 * v4 + 12345
        v4 = np.int32(v4)
    v10[v3] = chr(v5 ^ (v4 & 0xff))

print(b'Password: ' + ''.join(v10).encode());
