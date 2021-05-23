/*
If initially, a=1, b=1, c=3 and result=999, what is the value of result after the following C statement is executed(in decimal)?

result = b + 1 | c + a;
*/

#include <stdio.h>

int main(void)
{
    int a = 1;
    int b = 1;
    int c = 3;
    int result = 999;

    result = b + 1 | c + a;
    printf("%d\n", result);
}