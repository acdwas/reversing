
from z3 import *
from pwn import *

l = [0x05, 0x1D, 0x0D, 0x04, 0x10, 0x72, 0x00]

s = Solver()

a = [BitVec('a{}'.format(i), 8) for i in range(7)]
b = [BitVec('b{}'.format(i), 8) for i in range(7)]

for i in range(7):
    s.add(a[i] >= 0x30, a[i] <= 0x7a)
    s.add(b[i] >= 0x30, b[i] <= 0x7a)
    s.add(a[i] ^ b[i] == l[i])

while s.check() == sat:
    m = s.model()

    w = ''
    w1 = ''
    for i in range(7):
        w += chr(m[a[i]].as_long())
        w1 += chr(m[b[i]].as_long())
    p = process('./a.out')
    p.recvuntil('name:\n')
    p.sendline(w)
    p.recvuntil('name:\n')
    p.sendline(w1)
    s = p.recv()
    if b'Hello Boss' in s:
        print(w)
        print(w1)
        print(s)
        break
    p.close()

    s.add(Or(a[0] != s.model()[a[0]],
             a[1] != s.model()[a[1]],
             a[2] != s.model()[a[2]],
             a[3] != s.model()[a[3]],
             a[4] != s.model()[a[4]],
             a[5] != s.model()[a[5]],
             a[6] != s.model()[a[6]],
             b[0] != s.model()[b[0]],
             b[1] != s.model()[b[1]],
             b[2] != s.model()[b[2]],
             b[3] != s.model()[b[3]],
             b[4] != s.model()[b[4]],
             b[5] != s.model()[b[5]],
             b[6] != s.model()[b[6]],
             ))
