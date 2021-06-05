#include <stdio.h>

int main(int argc, char *argv[])
{
    char *input_filename = argv[1];  // name of input file
    char *output_filename = argv[2]; // name of output file
    // YOUR CODE HERE
    FILE *inputFilePtr;
    FILE *outputFilePtr;
    char num_str[11];
    char num_char;

    inputFilePtr = fopen(input_filename, "r");
    outputFilePtr = fopen(output_filename, "w");
    while (fscanf(inputFilePtr, "%s", num_str) != EOF)
    {
        num_char = num_str[0];
        fprintf(outputFilePtr, "%c", num_char);
        for (int i = 1; i < 3; i++)
        {
            fprintf(outputFilePtr, "%c", num_str[i]);
        }
        fprintf(outputFilePtr, "-");
        for (int i = 3; i < 7; i++)
        {
            fprintf(outputFilePtr, "%c", num_str[i]);
        }
        fprintf(outputFilePtr, "-");
        for (int i = 7; i < 11; i++)
        {
            fprintf(outputFilePtr, "%c", num_str[i]);
        }
        fprintf(outputFilePtr, "\n");
    }
    fclose(inputFilePtr);
    fclose(outputFilePtr);
}
