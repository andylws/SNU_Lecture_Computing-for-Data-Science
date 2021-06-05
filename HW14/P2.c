#include <stdio.h>

int main(int argc, char *argv[])
{
    char *input_filename = argv[1]; // name of input file
    // YOUR CODE HERE
    FILE *inputFilePtr;
    int sum = 0;
    int cur = 0;

    inputFilePtr = fopen(input_filename, "r");
    while (fscanf(inputFilePtr, "%d", &cur) != EOF)
    {
        sum = sum + cur;
    }

    printf("%d\n", sum);

    return 0;
}
