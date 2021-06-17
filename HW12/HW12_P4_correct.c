#include <stdio.h>
#include <stdlib.h>

int P4(int n);
int selfsum(int k);

int selfsum(int k)
{
    int sum = k;
    while (k != 0)
    {
        sum += k % 10;
        k /= 10;
    }

    return sum;
}

int P4(int n)
{

    int ans = n + 1;
    while (1)
    {
        int isSelfNum = 1;
        for (int i = 1; i < ans; i++)
        {
            if (selfsum(i) == ans)
            {
                isSelfNum = 0;
                break;
            }
        }
        if (isSelfNum)
        {
            return ans;
        }
        else
        {
            ans += 1;
        }
    }
}

// DO NOT MODIFY BELOW!
int main(int argc, char *argv[])
{
    int n = atoi(argv[1]);
    int ans = P4(n);

    printf("%d\n", ans);

    return 0;
}
