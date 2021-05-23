#include <stdio.h>

int main(void)
{
    int t = 2;
    {
        printf("%d\n", t);
        {
            printf("%d\n", t);
            t = 3;
        }
        printf("%d\n", t);
    }
    {
        printf("%d\n", t);
    }
}