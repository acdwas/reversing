fx:
        push    rbp
        mov     rbp, rsp
        mov     QWORD PTR [rbp-24], rdi
        mov     rax, QWORD PTR [rbp-24]
        mov     eax, DWORD PTR [rax]
        cmp     eax, 70
        jne     .L2
        mov     rax, QWORD PTR [rbp-24]
        add     rax, 4
        mov     eax, DWORD PTR [rax]
        cmp     eax, 76
        jne     .L2
        mov     rax, QWORD PTR [rbp-24]
        add     rax, 8
        mov     eax, DWORD PTR [rax]
        add     eax, eax
        cmp     eax, 130
        jne     .L2
        mov     rax, QWORD PTR [rbp-24]
        add     rax, 12
        mov     eax, DWORD PTR [rax]
        cmp     eax, 71
        jne     .L2
        mov     rax, QWORD PTR [rbp-24]
        add     rax, 16
        mov     eax, DWORD PTR [rax]
        cmp     eax, 123
        jne     .L2
        mov     rax, QWORD PTR [rbp-24]
        add     rax, 20
        mov     eax, DWORD PTR [rax]
        cmp     eax, 95
        jne     .L2
        mov     rax, QWORD PTR [rbp-24]
        add     rax, 24
        mov     eax, DWORD PTR [rax]
        sub     eax, 75
        cmp     eax, 2
        ja      .L2
        mov     rax, QWORD PTR [rbp-24]
        add     rax, 28
        mov     eax, DWORD PTR [rax]
        cmp     eax, 48
        jle     .L2
        mov     rax, QWORD PTR [rbp-24]
        add     rax, 32
        mov     eax, DWORD PTR [rax]
        cmp     eax, 100
        jle     .L2
        mov     rax, QWORD PTR [rbp-24]
        add     rax, 28
        mov     edx, DWORD PTR [rax]
        mov     rax, QWORD PTR [rbp-24]
        add     rax, 32
        mov     eax, DWORD PTR [rax]
        add     eax, edx
        cmp     eax, 152
        jne     .L2
        mov     rax, QWORD PTR [rbp-24]
        add     rax, 36
        mov     eax, DWORD PTR [rax]
        cmp     eax, 98
        jne     .L2
        mov     rax, QWORD PTR [rbp-24]
        add     rax, 40
        mov     eax, DWORD PTR [rax]
        test    eax, eax
        je      .L2
        mov     rax, QWORD PTR [rbp-24]
        add     rax, 44
        mov     eax, DWORD PTR [rax]
        cmp     eax, 48
        jne     .L2
        mov     rax, QWORD PTR [rbp-24]
        add     rax, 48
        mov     eax, DWORD PTR [rax]
        cmp     eax, 110
        jne     .L2
        mov     rax, QWORD PTR [rbp-24]
        add     rax, 52
        mov     eax, DWORD PTR [rax]
        cmp     eax, 95
        jne     .L2
        mov     rax, QWORD PTR [rbp-24]
        add     rax, 56
        mov     eax, DWORD PTR [rax]
        cmp     eax, 83
        jne     .L2
        mov     rax, QWORD PTR [rbp-24]
        add     rax, 60
        mov     eax, DWORD PTR [rax]
        cmp     eax, 104
        jne     .L2
        mov     rax, QWORD PTR [rbp-24]
        add     rax, 64
        mov     eax, DWORD PTR [rax]
        cmp     eax, 49
        jne     .L2
        mov     rax, QWORD PTR [rbp-24]
        add     rax, 68
        mov     eax, DWORD PTR [rax]
        cmp     eax, 110
        jne     .L2
        mov     rax, QWORD PTR [rbp-24]
        add     rax, 72
        mov     eax, DWORD PTR [rax]
        cmp     eax, 105
        jne     .L2
        mov     rax, QWORD PTR [rbp-24]
        add     rax, 76
        mov     eax, DWORD PTR [rax]
        cmp     eax, 110
        jne     .L2
        mov     rax, QWORD PTR [rbp-24]
        add     rax, 80
        mov     eax, DWORD PTR [rax]
        cmp     eax, 103
        jne     .L2
        mov     rax, QWORD PTR [rbp-24]
        add     rax, 84
        mov     eax, DWORD PTR [rax]
        cmp     eax, 95
        jne     .L2
        mov     rax, QWORD PTR [rbp-24]
        add     rax, 88
        mov     eax, DWORD PTR [rax]
        cmp     eax, 125
        jne     .L2
        mov     eax, 1
        jmp     .L3
.L2:
        mov     eax, 0
.L3:
        mov     DWORD PTR [rbp-4], eax
        nop
        pop     rbp
        ret
