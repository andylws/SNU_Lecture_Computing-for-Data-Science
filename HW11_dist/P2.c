/* Description
 * Write a program that reads any english alphabet from the keyboard 
 * and prints every character from that character down 
 * to the character A in the order in which they appear in the ASCII table
 */

#include <stdio.h>

void main(int argc, char *argv[])
{
	/* Please write your code below */
	char input_char;

	printf("Enter any alphabet:");
	scanf("%c", &input_char);

	while (input_char >= 'A')
	{
		printf("%c", input_char);
		input_char--;
	}

	/* Do not modify below */
}
