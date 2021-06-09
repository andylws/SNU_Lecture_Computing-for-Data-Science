/* Description
* Write a fibonacci function to calculate as following:
* f(n) = f(n-1) + f(n-2)
* with f(0) = 1, f(1) = 1
*/

#include <stdio.h>

/* Please write your code below */
int fibonacci(int n)
{
    if (n <= 1)
        return 1;

    int ans;

    ans = fibonacci(n - 1) + fibonacci(n - 2);

    return ans;
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

    f = fibonacci(n);
    printf("%d\n", f);
}