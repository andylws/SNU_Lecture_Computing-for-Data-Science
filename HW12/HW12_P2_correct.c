#include <stdio.h>
#include <stdlib.h>

int P2(int n);
int check(int n, int k);

int check(int n, int k)
{
    for (int i = 1; i <= n; i++)
    {
        if (k % i != 0)
        {
            return 0;
        }
    }
    return 1;
}

int P2(int n)
{

    int k = n;
    while (1)
    {
        if (check(n, k))
        {
            return k;
        }
        else
        {
            k++;
        }
    }
}

// DO NOT MODIFY BELOW!
int main(int argc, char *argv[])
{
    int n = atoi(argv[1]);
    int ans = P2(n);

    printf("%d\n", ans);

    return 0;
}
