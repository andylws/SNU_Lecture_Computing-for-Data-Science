/*
What should be written in "HERE" of the code, to have below result?

K
J
I
H
G
F
E
D
C
B
A
*/

#include <stdio.h>
#define STOP 0

int main(void)
{
    int counter;
    int startPoint;

    printf("==== Countdown Program ====\n");
    printf("Enter a positive integer: ");
    scanf("%d", &startPoint);

    for (counter = startPoint; counter >= STOP; counter--)
        // HERE
        printf("%c\n", counter + 'A');
}