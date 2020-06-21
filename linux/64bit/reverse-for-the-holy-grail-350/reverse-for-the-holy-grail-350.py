
firstchar = [0x41, 0x69, 0x6e, 0x45, 0x6f, 0x61]
thirdchar = [0x2ef, 0x2c4, 0x2dc, 0x2c7, 0x2de, 0x2fc]
masterArray = [0x1d7, 0x0c, 0x244, 0x25e, 0x093, 0x6c]

key = [0x20] * 19
x = 0
for i in range(18):
    if i % 3 == 0:
        key[i] = firstchar[x]
        x += 1

v = []
v7 = 0x29A
for i in range(19):
    v.append(v7)
    v7 += v7 % 5

v11 = 0
v7 = 0x29A
x = 0
for i in range(19):
    if v11 == 2:
        key[i] = v[i] ^ thirdchar[x]
        x += 1
        v11 = 0
    else:
        v11 += 1

x = 0
for i in range(0, 18, 3):
    for a in range(58, 128):
        if ((key[i] ^ v[i])*(a ^ v[i+1])) % thirdchar[x] == masterArray[x]:
            key[i+1] = a
            break
    x += 1

print('Password : ', ''.join(chr(i) for i in key))


# What... is your name?
# aaa
# What... is your quest?
# aaa
# What...  is the secret password?
# AfricanOrEuropean?
# Go on. Off you go. tuctf{AfricanOrEuropean?}
