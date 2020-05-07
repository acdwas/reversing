
from z3 import *
from pwn import *

s = Solver()

a = [BitVec('a{}'.format(i), 32) for i in range(32)]

for i in range(32):
    s.add(a[i] > 63, a[i] <= 90)

v3 = 247

for i in range(1, 32):
    v3 += If(a[i] <= 77, a[i] + 181, a[i] + 177) - i + 247

s.add(And(v3 % 248 == If(a[0] <= 77, a[i] + 181, a[i] + 177), v3 % 248 == 247))

while s.check() == sat:
    m = s.model()

    w = ''
    for i in range(32):
        w += chr(m[a[i]].as_long())
    p = process('./flag_keygen')
    p.recvline()
    p.sendline(w)
    r = p.recv()
    if b'Valid' in r:
        print(w)
        break
    p.close()

    s.add(Or(a[0] != s.model()[a[0]],
             a[1] != s.model()[a[1]],
             a[2] != s.model()[a[2]],
             a[3] != s.model()[a[3]],
             a[4] != s.model()[a[4]],
             a[5] != s.model()[a[5]],
             a[6] != s.model()[a[6]],
             a[7] != s.model()[a[7]],
             a[8] != s.model()[a[8]],
             a[9] != s.model()[a[9]],
             a[10] != s.model()[a[10]],
             a[11] != s.model()[a[11]],
             a[12] != s.model()[a[12]],
             a[13] != s.model()[a[13]],
             a[14] != s.model()[a[14]],
             a[15] != s.model()[a[15]],
             a[16] != s.model()[a[16]],
             a[17] != s.model()[a[17]],
             a[18] != s.model()[a[18]],
             a[19] != s.model()[a[19]],
             a[20] != s.model()[a[20]],
             a[21] != s.model()[a[21]],
             a[22] != s.model()[a[22]],
             a[23] != s.model()[a[23]],
             a[24] != s.model()[a[24]],
             a[25] != s.model()[a[25]],
             a[26] != s.model()[a[26]],
             a[27] != s.model()[a[27]],
             a[28] != s.model()[a[28]],
             a[29] != s.model()[a[29]],
             a[30] != s.model()[a[30]],
             a[31] != s.model()[a[31]]
             ))
