#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

int P4(int n);
int sumIndivDigits(int input_i);

// Implement P4
// You can define other function, but P4 must return answer.
int sumIndivDigits(int input_i)
{
    if (input_i < 10)
    {
        return input_i;
    }
    return sumIndivDigits(input_i / 10) + (input_i % 10);
}

int P4(int n)
{
    bool self_num = false;

    while (!self_num)
    {
        self_num = true;
        n++;
        for (int i = 1; i < n; i++)
        {
            int sum_indiv_digits = sumIndivDigits(i);
            if (i + sum_indiv_digits == n)
            {
                self_num = false;
                break;
            }
        }
    }

    return n;
}

// DO NOT MODIFY BELOW!
int main(int argc, char *argv[])
{
    int n = atoi(argv[1]);
    int ans = P4(n);

    printf("%d\n", ans);

    return 0;
}