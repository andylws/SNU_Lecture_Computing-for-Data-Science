/* Description
* Write a program that reads any english alphabet from the keyboard
* and prints every character from that character down
* to the character A in the order in which they appear in the ASCII table
*/

#include <stdio.h>

void main(int argc, char *argv[])
{
    /* Please write your code below */
    char counter;    //Holds intermediate count values
    char input_char; //Starting point for count down

    //Prompt the user for input
    printf("Enter any alphabet: ");
    scanf("%c", &input_char);

    //Count down from the input character to endpoint
    for (counter = input_char; counter >= 'A'; counter--)
        printf("%c", counter);

    /* Do not modify below */
}
