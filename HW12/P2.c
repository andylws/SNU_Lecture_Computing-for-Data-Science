#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

int P2(int n);

// Implement P2
// You can define other function, but P2 must return answer.
int P2(int n)
{
    bool done = false;
    int result = 0;

    while (!done)
    {
        done = true;
        result++;
        for (int i = 1; i <= n; i++)
        {
            if (result % i != 0)
            {
                done = false;
                break;
            }
        }
    }

    return result;
}

// DO NOT MODIFY BELOW!
int main(int argc, char *argv[])
{
    int n = atoi(argv[1]);
    int ans = P2(n);

    printf("%d\n", ans);

    return 0;
}