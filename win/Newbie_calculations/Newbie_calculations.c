
#include <stdio.h>

int sub_401220(int a1, int a2)
{
    return a1 - ((2147483647 - (-a2 - -2147483648)) + 1);
}

int sub_401000(int a1, int a2)
{
  return a1 + ((2147483647 - (-a2 - -2147483648)) + 1);
}

int sub_401100(int a1, int a2)
{
    return a1 * ((2147483647 - (-a2 - -2147483648)) + 1);
}

int main()
{
  signed int i; // [sp+4h] [bp-90h]@1
  signed int j; // [sp+8h] [bp-8Ch]@4
  int v117[33]; // [sp+Ch] [bp-88h]@3

  for ( i = 0; i < 32; ++i )
    v117[i] = 1;
  v117[32] = 0;
  printf("Your flag is: ");
  v117[0] = sub_401100(v117[0], 1000000000);
  v117[0] = sub_401220(v117[0], 999999950);
  v117[0] = sub_401100(v117[0], 2);
  v117[1] = sub_401000(v117[1], 5000000);
  v117[1] = sub_401220(v117[1], 6666666);
  v117[1] = sub_401000(v117[1], 1666666);
  v117[1] = sub_401000(v117[1], 45);
  v117[1] = sub_401100(v117[1], 2);
  v117[1] = sub_401000(v117[1], 5);
  v117[2] = sub_401100(v117[2], 1000000000);
  v117[2] = sub_401220(v117[2], 999999950);
  v117[2] = sub_401100(v117[2], 2);
  v117[2] = sub_401000(v117[2], 2);
  v117[3] = sub_401000(v117[3], 55);
  v117[3] = sub_401220(v117[3], 3);
  v117[3] = sub_401000(v117[3], 4);
  v117[3] = sub_401220(v117[3], 1);
  v117[4] = sub_401100(v117[4], 100000000);
  v117[4] = sub_401220(v117[4], 99999950);
  v117[4] = sub_401100(v117[4], 2);
  v117[4] = sub_401000(v117[4], 2);
  v117[5] = sub_401220(v117[5], 1);
  v117[5] = sub_401100(v117[5], 1000000000);
  v117[5] = sub_401000(v117[5], 55);
  v117[5] = sub_401220(v117[5], 3);
  v117[6] = sub_401100(v117[6], 1000000);
  v117[6] = sub_401220(v117[6], 999975);
  v117[6] = sub_401100(v117[6], 4);
  v117[7] = sub_401000(v117[7], 55);
  v117[7] = sub_401220(v117[7], 33);
  v117[7] = sub_401000(v117[7], 44);
  v117[7] = sub_401220(v117[7], 11);
  v117[8] = sub_401100(v117[8], 10);
  v117[8] = sub_401220(v117[8], 5);
  v117[8] = sub_401100(v117[8], 8);
  v117[8] = sub_401000(v117[8], 9);
  v117[9] = sub_401000(v117[9], 0);
  v117[9] = sub_401220(v117[9], 0);
  v117[9] = sub_401000(v117[9], 11);
  v117[9] = sub_401220(v117[9], 11);
  v117[9] = sub_401000(v117[9], 53);
  v117[10] = sub_401000(v117[10], 49);
  v117[10] = sub_401220(v117[10], 2);
  v117[10] = sub_401000(v117[10], 4);
  v117[10] = sub_401220(v117[10], 2);
  v117[11] = sub_401100(v117[11], 1000000);
  v117[11] = sub_401220(v117[11], 999999);
  v117[11] = sub_401100(v117[11], 4);
  v117[11] = sub_401000(v117[11], 50);
  v117[12] = sub_401000(v117[12], 1);
  v117[12] = sub_401000(v117[12], 1);
  v117[12] = sub_401000(v117[12], 1);
  v117[12] = sub_401000(v117[12], 1);
  v117[12] = sub_401000(v117[12], 1);
  v117[12] = sub_401000(v117[12], 1);
  v117[12] = sub_401000(v117[12], 10);
  v117[12] = sub_401000(v117[12], 32);
  v117[13] = sub_401100(v117[13], 10);
  v117[13] = sub_401220(v117[13], 5);
  v117[13] = sub_401100(v117[13], 8);
  v117[13] = sub_401000(v117[13], 9);
  v117[13] = sub_401000(v117[13], 48);
  v117[14] = sub_401220(v117[14], 1);
  v117[14] = sub_401100(v117[14], -294967296);
  v117[14] = sub_401000(v117[14], 55);
  v117[14] = sub_401220(v117[14], 3);
  v117[15] = sub_401000(v117[15], 1);
  v117[15] = sub_401000(v117[15], 2);
  v117[15] = sub_401000(v117[15], 3);
  v117[15] = sub_401000(v117[15], 4);
  v117[15] = sub_401000(v117[15], 5);
  v117[15] = sub_401000(v117[15], 6);
  v117[15] = sub_401000(v117[15], 7);
  v117[15] = sub_401000(v117[15], 20);
  v117[16] = sub_401100(v117[16], 10);
  v117[16] = sub_401220(v117[16], 5);
  v117[16] = sub_401100(v117[16], 8);
  v117[16] = sub_401000(v117[16], 9);
  v117[16] = sub_401000(v117[16], 48);
  v117[17] = sub_401000(v117[17], 7);
  v117[17] = sub_401000(v117[17], 6);
  v117[17] = sub_401000(v117[17], 5);
  v117[17] = sub_401000(v117[17], 4);
  v117[17] = sub_401000(v117[17], 3);
  v117[17] = sub_401000(v117[17], 2);
  v117[17] = sub_401000(v117[17], 1);
  v117[17] = sub_401000(v117[17], 20);
  v117[18] = sub_401000(v117[18], 7);
  v117[18] = sub_401000(v117[18], 2);
  v117[18] = sub_401000(v117[18], 4);
  v117[18] = sub_401000(v117[18], 3);
  v117[18] = sub_401000(v117[18], 6);
  v117[18] = sub_401000(v117[18], 5);
  v117[18] = sub_401000(v117[18], 1);
  v117[18] = sub_401000(v117[18], 20);
  v117[19] = sub_401100(v117[19], 1000000);
  v117[19] = sub_401220(v117[19], 999999);
  v117[19] = sub_401100(v117[19], 4);
  v117[19] = sub_401000(v117[19], 50);
  v117[19] = sub_401220(v117[19], 1);
  v117[20] = sub_401220(v117[20], 1);
  v117[20] = sub_401100(v117[20], -294967296);
  v117[20] = sub_401000(v117[20], 49);
  v117[20] = sub_401220(v117[20], 1);
  v117[21] = sub_401220(v117[21], 1);
  v117[21] = sub_401100(v117[21], 1000000000);
  v117[21] = sub_401000(v117[21], 54);
  v117[21] = sub_401220(v117[21], 1);
  v117[21] = sub_401000(v117[21], 1000000000);
  v117[21] = sub_401220(v117[21], 1000000000);
  v117[22] = sub_401000(v117[22], 49);
  v117[22] = sub_401220(v117[22], 1);
  v117[22] = sub_401000(v117[22], 2);
  v117[22] = sub_401220(v117[22], 1);
  v117[23] = sub_401100(v117[23], 10);
  v117[23] = sub_401220(v117[23], 5);
  v117[23] = sub_401100(v117[23], 8);
  v117[23] = sub_401000(v117[23], 9);
  v117[23] = sub_401000(v117[23], 48);
  v117[24] = sub_401000(v117[24], 1);
  v117[24] = sub_401000(v117[24], 3);
  v117[24] = sub_401000(v117[24], 3);
  v117[24] = sub_401000(v117[24], 3);
  v117[24] = sub_401000(v117[24], 6);
  v117[24] = sub_401000(v117[24], 6);
  v117[24] = sub_401000(v117[24], 6);
  v117[24] = sub_401000(v117[24], 20);
  v117[25] = sub_401000(v117[25], 55);
  v117[25] = sub_401220(v117[25], 33);
  v117[25] = sub_401000(v117[25], 44);
  v117[25] = sub_401220(v117[25], 11);
  v117[25] = sub_401000(v117[25], 42);
  v117[26] = sub_401000(v117[26], v117[25]);
  v117[27] = sub_401000(v117[27], v117[12]);
  v117[28] = sub_401220(v117[28], 1);
  v117[28] = sub_401000(v117[28], v117[27]);
  v117[28] = sub_401220(v117[28], 1);
  v117[29] = sub_401220(v117[29], 1);
  v117[29] = sub_401100(v117[29], 1000000);
  v117[29] = sub_401000(v117[29], v117[23]);
  v117[30] = sub_401000(v117[30], 1);
  v117[30] = sub_401100(v117[30], v117[27]);
  v117[31] = sub_401000(v117[31], v117[30]);
  printf("CTF{");
  for ( j = 0; j < 32; ++j )
    printf("%c", v117[j]);
  printf("}\n");
  return 0;
}