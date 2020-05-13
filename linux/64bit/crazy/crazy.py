
k = '327a6c4304ad5938eaf0efb6cc3e53dc'

p = ''

for j in k:
    for i in range(0x20, 0x7f):
        w = chr((i ^ 0x50) + 0x17)
        w = chr((ord(w) ^ 0x13) + 0xb)
        if w == j:
            p += chr(i)
            break

print('Pass: ' + p)
