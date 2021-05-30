#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

int P3(int n);

// Implement P3
// You can define other function, but P3 must return answer.
int P3(int n)
{

    int count = 0;

    for (int i = n + 1; i < 2 * n; i++)
    {
        bool is_prime = true;
        for (int j = 2; j <= i / 2; j++)
        {
            if (i % j == 0)
            {
                is_prime = false;
                break;
            }
        }
        if (is_prime)
        {
            count++;
        }
    }

    return count;
}

// DO NOT MODIFY BELOW!
int main(int argc, char *argv[])
{
    int n = atoi(argv[1]);
    int ans = P3(n);

    printf("%d\n", ans);

    return 0;
}