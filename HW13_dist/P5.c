#include <stdio.h>
#include <stdlib.h>
#define MAX_LEN 10

char *SwitchCase(char *s);
int main(int argc, char *argv[])
{
  char *str; //List of characters to be sorted

  str = argv[1];
  printf("%s", SwitchCase(str));
}
/* Do not modify above */
/* Write your code below */
char *SwitchCase(char *s)
{
  char *cur = s;
  while (*cur != '\0')
  {
    if (*cur > 96)
    {
      *cur = *cur - 32;
    }
    else
    {
      *cur = *cur + 32;
    }
    cur = cur + 1;
  }
  return s;
}