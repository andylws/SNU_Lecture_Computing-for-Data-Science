/*
What is printed if you run following code?
*/

#include <stdio.h>

int main(void)
{
    char letter = 'f';
    letter = ((letter >= 'a' && letter <= 'z') ? '!' : letter);
    printf("%c\n", letter);
}