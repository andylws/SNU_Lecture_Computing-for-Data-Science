/* Description
 * Write a function to return an natural number in base 4
 * (using only the digits 0,1,2,3) 
 */

#include <stdio.h>
#include <stdlib.h>

/* Please write your code below */
int base_four(int n)
{

	if (n < 4)
	{
		return n;
	}

	int remain = n % 4;

	return base_four(n / 4) * 10 + remain;
}
/* Do not modify below */

void main(int argc, char *argv[])
{

	if (argc != 2)
	{
		printf("Enter any natural number n\n");
	}

	int n = atoi(argv[1]);

	if (n < 0)
	{
		printf("No negative number is allowed\n");
	}

	int f = 0;

	f = base_four(n);
	printf("%d\n", f);
}
