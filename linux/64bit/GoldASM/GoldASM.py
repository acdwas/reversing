
from z3 import *
import subprocess

s = Solver()

a = [BitVec('a{}'.format(i), 8) for i in range(23)]

for i in range(22):
    s.add(a[i] >= 0x20, a[i] <= 0x7f)

s.add(a[0] == 70)
s.add(a[1] == 76)
s.add(2 * a[2] == 130)
s.add(a[3] == 71)
s.add(a[4] == 123)
s.add(a[5] == 95)
s.add(a[6] - 75 <= 2)
s.add(a[7] > 48)
s.add(a[8] > 100)
s.add(a[7] + a[8] == 152)
s.add(a[9] == 98)
s.add(a[10] != 0)
s.add(a[11] == 48)
s.add(a[12] == 110)
s.add(a[13] == 95)
s.add(a[14] == 83)
s.add(a[15] == 104)
s.add(a[16] == 49)
s.add(a[17] == 110)
s.add(a[18] == 105)
s.add(a[19] == 110)
s.add(a[20] == 103)
s.add(a[21] == 95)
s.add(a[22] == 125)

while s.check() == sat:
    m = s.model()

    w = ''
    for i in range(23):
        w += chr(m[a[i]].as_long())
    # print(w)

    process = subprocess.Popen(
        ['./a.out', w], stderr=subprocess.PIPE, stdout=subprocess.PIPE)
    stdout, stderr = process.communicate()
    exit_code = process.wait()
    if exit_code == 1:
        print(w)

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
             a[22] != s.model()[a[22]]
             ))
