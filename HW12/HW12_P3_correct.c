#include <stdio.h>
#include <stdlib.h>

int P3(int n);
int isPrime(int k);

int isPrime(int k)
{
    for (int i = 2; i < k; i++)
    {
        if (k % i == 0)
        {
            return 0;
        }
    }
    return 1;
}

int P3(int n)
{
    int ans = 0;
    for (int i = n + 1; i < 2 * n; i++)
    {
        if (isPrime(i))
        {
            ans++;
        }
    }
    return ans;
}

// DO NOT MODIFY BELOW!
int main(int argc, char *argv[])
{
    int n = atoi(argv[1]);
    int ans = P3(n);

    printf("%d\n", ans);

    return 0;
}