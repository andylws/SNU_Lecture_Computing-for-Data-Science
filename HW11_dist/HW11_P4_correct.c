/* Description
* Write a function to return an natural number in base 4
* (using only the digits 0,1,2,3)
*/

#include <stdio.h>

/* Please write your code below */
int base_four(int n)
{
    int r;
    int f = 0;
    int e = 1;
    while (n >= 4)
    {
        r = n % 4;
        n = (int)n / 4;
        f = f + e * r;
        e *= 10;
    }
    f += e * n;
    return f;
}
/* Do not modify below */

void main(int argc, char *argv[])
{

    if (argc != 2)
    {
        printf("Enter any natural number n\n");
    }

    int n = atoi(argv[1]);

    if (n < 0)
    {
        printf("No negative number is allowed\n");
    }

    int f = 0;

    f = base_four(n);
    printf("%d\n", f);
}