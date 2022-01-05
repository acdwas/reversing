
from Crypto.Cipher import AES
import sys

with open('./flag.txt', 'rb') as f:
    l = f.read()

key = bytes([i for i in range(0x10)])
iv = bytes([i for i in range(0x10)])


for i in range(120):
    for j in range(120):
        w = ''
        key = list(key)
        key[14] = i
        key[15] = j
        key = bytes(key)
        cipher = AES.new(key, AES.MODE_CBC, iv)
        w = cipher.decrypt(l)
        if b'flag' in w:
            print(key)
            print(w.decode())
            sys.exit()

# flag{k3y_l0gg3r_n_st34lth_m0d3}

