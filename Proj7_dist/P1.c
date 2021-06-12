#include <stdio.h>
#include <stdlib.h>

/*
  Print reversed linked list
*/

struct Node {
    int data;
    struct Node* next;
};

/* Create a new node */
struct Node * createNode(struct Node * newNode, int data){
  newNode = (struct Node *) malloc(sizeof(struct Node));
  newNode->data = data;
  return newNode;
}


int main(int argc, char* argv[])
{  
  int length = argc - 1;

  /* Create a linked list from input integers */
  int k = 1;
  struct Node * head = NULL;
  struct Node * prev = NULL;
  struct Node * curr = NULL;

addNode:
  curr = createNode(curr, atoi(argv[k]));  
    
  if (k > 1)
    prev->next = curr;
  else
    head = curr;

  k++;
  prev = curr;

  if (k <= length)
    goto addNode;

  /* Write your code here */	

  struct Node * nodeArray[length];

  curr = head;

  for (int i = 0; i < length; i++) {
    nodeArray[i] = curr;
    curr = curr->next;
  }

  for (int i = length - 1; i > 0; i--) {
    nodeArray[i]->next = nodeArray[i - 1];
  }

  nodeArray[0]->next = NULL;
  head = nodeArray[length - 1];

	/* Do not modify below */	
  curr = head;
  
  while (curr){
    printf("%d", curr->data);
    curr = curr->next;
  }

  return 0;


}


