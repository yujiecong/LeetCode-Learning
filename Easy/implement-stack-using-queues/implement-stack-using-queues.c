#include <stdio.h>
#include <stdlib.h>
typedef int bool;
typedef struct MyNode
{
    struct MyNode *next;
    int data;
} myNode;

typedef struct
{
    myNode *top;
} MyStack;

/** Initialize your data structure here. */

MyStack *myStackCreate()
{
    MyStack *stack = calloc(1, sizeof(MyStack));
    //stack->top = NULL;
    // calloc可以初始化置数
    return stack;
}

/** Push element x onto stack. */
void myStackPush(MyStack *obj, int x)
{
    myNode *q = (myNode *)malloc(sizeof(myNode));
    q->data = x;
    q->next = obj->top;

    obj->top = q;
}

/** Removes the element on top of the stack and returns that element. */
int myStackPop(MyStack *obj)
{
    myNode *topNode = obj->top;
    int data = topNode->data;
    obj->top = topNode->next;
    free(topNode);
    return data;
}

/** Get the top element. */
int myStackTop(MyStack *obj)
{
    return obj->top->data;
}

/** Returns whether the stack is empty. */
bool myStackEmpty(MyStack *obj)
{
    return (obj->top == NULL);
}

void myStackFree(MyStack *obj)
{
    myNode *node = NULL;
    while (node != NULL)
    {
        node = obj->top;
        free(node);
        node = obj->top->next;
    }
    free(obj);
}
void printStack(MyStack *obj)
{
    int data;
    printf("pop...\n");
    while (obj->top != NULL)
    {
        data = myStackPop(obj);
        printf("data=%d\n", data);
    }
}
/**
 * Your MyStack struct will be instantiated and called as such:
 * MyStack* obj = myStackCreate();
 * myStackPush(obj, x);
 
 * int param_2 = myStackPop(obj);
 
 * int param_3 = myStackTop(obj);
 
 * bool param_4 = myStackEmpty(obj);
 
 * myStackFree(obj);
*/
int main()
{
    MyStack *obj = myStackCreate();
    myStackPush(obj, 1);
    myStackPush(obj, 2);
    printf(" myStackTop(obj);=%d\n", myStackTop(obj));
    printf("myStackPop(obj);=%d\n", myStackPop(obj));
    myStackEmpty(obj);
}