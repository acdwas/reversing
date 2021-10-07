
from z3 import *
from pwn import *

# r = process('./simpleshell')

r = remote('bamboofox.cs.nctu.edu.tw', 10012)

r.recvuntil(b'(anonymous) # ')
r.sendline(b'info')
DAT_0804a54c = int(r.recvuntil(b'(anonymous) # ').split()[7])

s = Solver()

passwd = [ord(i) for i in 'DoYouThinkThisIsPassword']

a = [BitVec(f'a{i}', 8) for i in range(len(passwd))]


DAT_0804a548 = (DAT_0804a54c * 0xffff + 0x7a69) & 0xffffffff

for i in range(0, len(passwd), 4):
    edx = (DAT_0804a548 + 0xff) & 0xff
    a[i] = (((edx - 0xff) & 0xffffffff) ^ a[i]) & 0xff
    a[i+2] ^= 0x5f

for i in range(len(passwd)):
    s.add(a[i] == passwd[i])

print(s.check())
m = s.model()

flag = {}

for d in m.decls():
    flag[int(d.name()[1:])] = m[d].as_long()

w = ''

for i in sorted(flag):
    w += chr(flag[i])

ppp = w.encode()

r.sendline(b'login')
r.recvuntil(b'name: ')
r.sendline(b'admin')
r.recvuntil(b'password: ')
r.sendline(ppp)
r.recvuntil(b'(admin) # ')
r.sendline(b'flag')
print(r.recv())

# SECPROG{"This_time_HexRay_doesn't_work"}



