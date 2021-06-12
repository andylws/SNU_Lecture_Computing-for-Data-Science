#include <stdio.h>
#include <stdlib.h>


// A structure to represent a stack
struct Stack {
  int top;
  unsigned capacity;
  char* array;
};
 
// function to create a stack of given capacity. It initializes size of
// stack as 0
struct Stack* createStack(unsigned capacity)
{
  struct Stack* stack = (struct Stack*)malloc(sizeof(struct Stack));
  stack->capacity = capacity;
  stack->top = -1;
  stack->array = (char*)malloc(stack->capacity * sizeof(char));
  return stack;
}
 
// Stack is full when top is equal to the last index
int isFull(struct Stack* stack)
{
  return stack->top == stack->capacity - 1;
}
 
// Stack is empty when top is equal to -1
int isEmpty(struct Stack* stack)
{
  return stack->top == -1;
}
 
// Function to add an item to stack.  It increases top by 1
void push(struct Stack* stack, char item)
{
  if (isFull(stack))
    return;
  stack->array[++stack->top] = item;
}
 
// Function to remove an item from stack.  It decreases top by 1
char pop(struct Stack* stack)
{
  if (isEmpty(stack))
    return '0';
  return stack->array[stack->top--];
}

int main(int argc, char* argv[])
{  

  char* strInput = argv[1];
  int success = 0; // 0 on success, -1 on failure

  /* Write your code here */	

  struct Stack* stack = createStack(10);
  int i = 0;

  while(strInput[i] != '\0') {
    if (strInput[i] == '(' || strInput[i] == '{' || strInput[i] == '['){
      push(stack, strInput[i]);
    }
    else if (strInput[i] == ')') {
      if (isEmpty(stack)) {
        success = -1;
      }
      else if (stack->array[stack->top] == '(') {
        pop(stack);
      } 
      else {
        success = -1;
        break;
      }
    }
    else if (strInput[i] == '}') {
      if (isEmpty(stack)) {
        success = -1;
      }
      else if (stack->array[stack->top] == '{') {
        pop(stack);
      } 
      else {
        success = -1;
        break;
      }
    }
    else if (strInput[i] == ']') {
      if (isEmpty(stack)) {
        success = -1;
      }
      else if (stack->array[stack->top] == '[') {
        pop(stack);
      } 
      else {
        success = -1;
        break;
      }
    }
    else {
        printf("Wrong input!");
    }
    if (isFull(stack)) {
      struct Stack* newStack = createStack(2 * stack->capacity);
      for (int j = 0; j < stack->capacity; j++) {
        push(newStack, stack->array[j]);
      }
      stack = newStack;
      free(newStack);
    }
    i++;
  }


  if (!isEmpty(stack)) {
    success = -1;
  }

  /* Do not modify below */	
  printf("%d", success);

  return 0;
}


