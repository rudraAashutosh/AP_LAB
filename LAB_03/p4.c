// # Q-4. Design a Data Structure SpecialStack that supports all the stack operations like push(), pop(). impty(), 
// # isFull() and an additional operation getMin() which should return minimum element from the SpecialStack.
// # All these operations of SpecialStack must have a time and space complexity of 0(1).

// # Note: To implement SpecialStack, you should only use standard Stack data structure and no other data structura 
// # like arrays list ate

#include<stdio.h>
#define MAX 1000
typedef struct Stack
{
    int data;
    struct Stack*next;
    
    
}Stack;
int count=0;
Stack *head=NULL;
Stack *tail=NULL;
void push(int a)
{
  Stack *t;
  t=(Stack *)malloc(sizeof(Stack));
  t->data=a;
  t->next=NULL;
  if(head==NULL)
  {
    head=t;
    count++;
    tail=t;
  }
  else
  {
    tail->next=t;

    count++;
    tail=t;
  }
}



int pop()
{
    if(isEmpty==-1)
{count--;
  Stack *t=head;
  while(t->next!=tail)
  {
    t=t->next;
  }

  return tail->data;}

  else
    return 0;
}

int isEmpty()
{
    if(head==NULL)
    {

        return 1;
    }
    else
        return -1;
}

int is_Full()
{
    if(count==MAX)
    return 1;
    else
    return 0;
}
