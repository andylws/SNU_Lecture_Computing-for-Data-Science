#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[])
{
    int N = atoi(argv[1]);
    // YOUR CODE HERE

    for (int i = 0; i < N; i++)
    {
        for (int j1 = 0; j1 < N - i - 1; j1++)
        {
            printf(" ");
        }
        for (int j2 = 0; j2 < 2 * i + 1; j2++)
        {
            printf("*");
        }
        printf("\n");
    }

    return 0;
}