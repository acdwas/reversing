
l = [0xBC, 0x52, 0xE8, 0xEA, 0x50, 0xEA, 0xE8, 0xA7, 0xE8, 0xEA, 0x93, 0x52, 0xE8, 0xEA, 0x50, 0xEA, 0xE8, 0xDF, 0xE8, 0xEA, 0xDF, 0x52, 0xE8, 0xEA, 0x50, 0xEA, 0xE8, 0xDA, 0xE8, 0xEA, 0xDA, 0x52, 0xE8, 0xEA, 0x50, 0xEA, 0xE8, 0xD2, 0xE8, 0xEA, 0xD0, 0x52, 0xE8, 0xEA, 0x50, 0xEA, 0xE8, 0xDD,
     0xE8, 0xEA, 0xC4, 0x52, 0xE8, 0xEA, 0x50, 0xEA, 0xE8, 0xD3, 0xE8, 0xEA, 0xDA, 0x52, 0xE8, 0xEA, 0x50, 0xEA, 0xE8, 0xD8, 0xE8, 0xEA, 0xDF, 0x52, 0xE8, 0xEA, 0x50, 0xEA, 0xE8, 0xDE, 0xE8, 0xEA, 0xDE, 0x52, 0xE8, 0xEA, 0x50, 0xEA, 0xE8, 0xDF, 0xE8, 0xEA, 0x95, 0x52, 0xE8, 0xEA, 0xEA, 0x00]

ll = l

for a1 in range(256):
    l = ll
    for v26 in range(40):
        for i in range(v26):
            l[2*i] += 1
            l[2*i+1] += 1

        j = 0
        while True:
            if j < 0x5f and j != 0x5e:
                l[j] ^= l[j+1]
                l[j+1] ^= l[j]
                l[j] ^= l[j+1]
                if j < 2 * v26:
                    l[j] -= 1
            else:
                break
            j += 2

        for i in range(v26):
            l[2 * i + 1] -= 1

        for j in range(0x5F):
            if (j % 2):
                l[j] ^= a1 - 1
            else:
                l[j] ^= a1 + 1

        v1 = 0
        for i in range(0x5f):
            v1 += l[i]
        if v1 == 4693:
            print(v26, a1, 'FLAG: '+''.join(chr(i)
                                            for i in l if 0x20 < i < 0x7f))


# FLAG: TM{5702887,9227465}
