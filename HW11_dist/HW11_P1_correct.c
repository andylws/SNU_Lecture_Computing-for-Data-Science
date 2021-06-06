/* Description
* Write a program that reads a positive integer from the keyboard
* and displays a 1 if it is divisible by 3 or a 0 otherwise
*/

#include <stdio.h>

void main(int argc, char *argv[])
{
    int input_int;
    int ans = -1;
    /* Please write your code below */
    printf("Enter any natural number:");

    scanf("%d", &input_int);
    if (input_int % 3 == 0)
    {
        ans = 1;
    }
    else
    {
        ans = 0;
    }

    /* Do not modify below */
    printf("ans:%d\n", ans);
}
