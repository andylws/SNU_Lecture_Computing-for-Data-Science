/*
Which of the following statement have different value of j after execution?
*/

#include <stdio.h>

int main(void)
{
    {
        int i1 = 10;
        int j1 = 0;

        i1 += 1;
        j1 = i1;
        printf("1. %d\n", j1);
    }
    {
        int i2 = 10;
        int j2 = 0;

        j2 = i2 += 1;
        printf("2. %d\n", j2);
    }
    {
        int i3 = 10;
        int j3 = 0;

        j3 = i3++;
        printf("3. %d\n", j3);
    }
    {
        int i4 = 10;
        int j4 = 0;

        j4 = i4 + 1;
        printf("4. %d\n", j4);
    }
    {
        int i5 = 10;
        int j5 = 0;

        j5 = ++i5;
        printf("5. %d\n", j5);
    }
}