
from z3 import *

with open('FirstStepsOnWindows.exe', 'rb') as f:
    l = bytearray(f.read())

    b1 = l[0x27AA8:0x27AA8+33]
    b2 = l[0x27A84:0x27A84+33]

    s = Solver()

    a = [BitVec('a{}'.format(i), 8) for i in range(33)]

    x = 0

    for i in range(33):
        y = a[i] ^ b1[i] ^ b2[i]
        x |= y

    s.add(x == 0)
    s.check()
    m = s.model()
    print(''.join(chr(m[a[i]].as_long()) for i in range(33)))
