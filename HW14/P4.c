#include <stdio.h>

int main(int argc, char *argv[])
{
    char *input_filename = argv[1];  // name of input file
    char *output_filename = argv[2]; // name of output file
    // YOUR CODE HERE
    FILE *inputFilePtr;
    FILE *outputFilePtr;
    int num = 0;

    inputFilePtr = fopen(input_filename, "r");
    outputFilePtr = fopen(output_filename, "w");

    while (fscanf(inputFilePtr, "%d", &num) != EOF)
    {
        fprintf(outputFilePtr, "%d = ", num);
        for (int i = 2; i <= num; i++)
        {
            while (num % i == 0)
            {
                if (num / i == 1)
                {
                    fprintf(outputFilePtr, "%d", i);
                    break;
                }
                num = num / i;
                fprintf(outputFilePtr, "%d * ", i);
            }
        }
        fprintf(outputFilePtr, "\n");
    }

    return 0;
}
