#include <stdio.h>
#include <stdlib.h>


int byte_804869C[] = {  '\x6A', '\xFB', '\x4C', '\x8D', '\x58',
                        '\x0F', '\xD4', '\xE8', '\x94', '\x98',
                        '\xEE', '\x6B', '\x18', '\x30', '\xE0',
                        '\x55', '\xC5', '\x28', '\x0E', '\x90' };

int main(void)
{
    int v1;
    signed int v2; // esi@4
    int v3; // edx@5
    int v4; // eax@5
    char v5; // cl@5
    int v7; // edx@5
    int v9; // [sp+18h] [bp-8Ch]@5
    char v10[124]; // [sp+28h] [bp-7Ch]@1

    for(v1=0;v1<19;v1++)
    {
        v10[v1] = '.';
    }
    v10[19] = '\0';
    v2 = 10;
    do
    {
        v3 = random() % 19;
        v4 = 0;
        v5 = byte_804869C[v3];
        v9 = v3 + 1;
        v7 = 0;
        while ( v7 < v9 )
        {
          ++v7;
          v4 = 1828812941 * v4 + 12345;
        }
        v10[v3] = v5 ^ (v4 & 0xff);
        --v2;
    }
    while ( v2 );
    printf("Password: %s\n", v10);
    return 0;
}
