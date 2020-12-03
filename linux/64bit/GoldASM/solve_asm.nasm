[bits 64]

section .text
    global _start
_start:

        mov rdi, [rsp+0x10]
        call fx

        mov r10, rax
        xor rax, rax

        mov rax, 60     ; exit call id
        mov rdi, r10      ; return success
        syscall

fx:
        push    rbp
        mov     rbp, rsp
        mov     QWORD  [rbp-24], rdi
        mov     rax, QWORD  [rbp-24]
        movzx     eax, BYTE  [rax]
        cmp     eax, 70
        jne     .L2
        mov     rax, QWORD  [rbp-24]
        add     rax, 1
        movzx     eax, BYTE  [rax]
        cmp     eax, 76
        jne     .L2
        mov     rax, QWORD  [rbp-24]
        add     rax, 2
        movzx     eax, BYTE  [rax]
        add     eax, eax
        cmp     eax, 130
        jne     .L2
        mov     rax, QWORD  [rbp-24]
        add     rax, 3
        movzx     eax, BYTE  [rax]
        cmp     eax, 71
        jne     .L2
        mov     rax, QWORD  [rbp-24]
        add     rax, 4
        movzx     eax, BYTE  [rax]
        cmp     eax, 123
        jne     .L2
        mov     rax, QWORD  [rbp-24]
        add     rax, 5
        movzx     eax, BYTE  [rax]
        cmp     eax, 95
        jne     .L2
        mov     rax, QWORD  [rbp-24]
        add     rax, 6
        movzx     eax, BYTE  [rax]
        sub     eax, 75
        cmp     eax, 2
        ja      .L2
        mov     rax, QWORD  [rbp-24]
        add     rax, 7
        movzx     eax, BYTE  [rax]
        cmp     eax, 48
        jle     .L2
        mov     rax, QWORD  [rbp-24]
        add     rax, 8
        movzx     eax, BYTE  [rax]
        cmp     eax, 100
        jle     .L2
        mov     rax, QWORD  [rbp-24]
        add     rax, 7
        movzx   edx, BYTE  [rax]
        mov     rax, QWORD  [rbp-24]
        add     rax, 8
        movzx     eax, BYTE  [rax]
        add     eax, edx
        cmp     eax, 152
        jne     .L2
        mov     rax, QWORD  [rbp-24]
        add     rax, 9
        movzx     eax, BYTE  [rax]
        cmp     eax, 98
        jne     .L2
        mov     rax, QWORD  [rbp-24]
        add     rax, 10
        movzx     eax, BYTE  [rax]
        test    eax, eax
        je      .L2
        mov     rax, QWORD  [rbp-24]
        add     rax, 11
        movzx     eax, BYTE  [rax]
        cmp     eax, 48
        jne     .L2
        mov     rax, QWORD  [rbp-24]
        add     rax, 12
        movzx     eax, BYTE  [rax]
        cmp     eax, 110
        jne     .L2
        mov     rax, QWORD  [rbp-24]
        add     rax, 13
        movzx     eax, BYTE  [rax]
        cmp     eax, 95
        jne     .L2
        mov     rax, QWORD  [rbp-24]
        add     rax, 14
        movzx     eax, BYTE  [rax]
        cmp     eax, 83
        jne     .L2
        mov     rax, QWORD  [rbp-24]
        add     rax, 15
        movzx     eax, BYTE  [rax]
        cmp     eax, 104
        jne     .L2
        mov     rax, QWORD  [rbp-24]
        add     rax, 16
        movzx     eax, BYTE  [rax]
        cmp     eax, 49
        jne     .L2
        mov     rax, QWORD  [rbp-24]
        add     rax, 17
        movzx     eax, BYTE  [rax]
        cmp     eax, 110
        jne     .L2
        mov     rax, QWORD  [rbp-24]
        add     rax, 18
        movzx     eax, BYTE  [rax]
        cmp     eax, 105
        jne     .L2
        mov     rax, QWORD  [rbp-24]
        add     rax, 19
        movzx     eax, BYTE  [rax]
        cmp     eax, 110
        jne     .L2
        mov     rax, QWORD  [rbp-24]
        add     rax, 20
        movzx     eax, BYTE  [rax]
        cmp     eax, 103
        jne     .L2
        mov     rax, QWORD  [rbp-24]
        add     rax, 21
        movzx     eax, BYTE  [rax]
        cmp     eax, 95
        jne     .L2
        mov     rax, QWORD  [rbp-24]
        add     rax, 22
        movzx     eax, BYTE  [rax]
        cmp     eax, 125
        jne     .L2
        mov     eax, 1
        jmp     .L3
.L2:
        mov     eax, 0
.L3:
        mov     DWORD  [rbp-4], eax
        nop
        pop     rbp
        ret
