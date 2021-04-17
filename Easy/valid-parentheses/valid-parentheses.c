#include <stdio.h>
#include <stdlib.h>
typedef int bool;
typedef struct Stack
{
    int top;
    char *data;
} mystack;

mystack *initStack(int leng)
{
    mystack *stack = (mystack *)malloc(sizeof(mystack));
    stack->data = (char *)malloc(sizeof(char) * leng);
    stack->top = 0;
    return stack;
}
//覆盖方法，空间其实还没被释放，只是栈顶指针的移动
void pop(mystack *s)
{
    if (s->top > 0)
    {
        s->top--;
        printf("pop ..%c \n", s->data[s->top]);
    }
}
void push(mystack *s, char str)
{

    s->data[s->top] = str;
    printf("push ..%c \n", s->data[s->top]);
    s->top++;
}
char getTop(mystack *s)
{
    if (s->top != 0)
        return s->data[s->top - 1];
    else
    {
        return '0';
    }
}
bool emptyStack(mystack *s)
{
    return (s->top == 0);
}
bool isValid(char *s)
{
    int leng = 0, flag = 0, flag1 = 0, flag2 = 0;
    char cur;
    for (int i = 0; s[i] != '\0'; i++, leng++)
        ;
    mystack *stack = initStack(leng);
    push(stack, s[0]);
    for (int i = 1; i < leng; i++)
    {
        cur = getTop(stack);
        switch (cur)
        {
        case '(':
            flag = 1;
            flag1 = 0;
            flag2 = 0;
            break;

            break;
        case '[':
            flag1 = 1;
            flag = 0;
            flag2 = 0;
            break;

        case '{':
            flag2 = 1;
            flag1 = 0;
            flag = 0;
            break;
        default:
            break;
        }
        push(stack, s[i]);
        switch (s[i])
        {
        case ')':
            if (flag)
            {
                pop(stack);
                pop(stack);
            }
            break;
        case ']':

            if (flag1)
            {
                pop(stack);
                pop(stack);
            } 
            break;
        case '}':
            if (flag2)
            {
                pop(stack);
                pop(stack);
            }
        default:
            break;
        }
        flag2 = 0;
        flag1 = 0;
        flag = 0;
    }
    return emptyStack(stack);
}

int main()
{
    char str[] = "()[]{}";
    test(str);
    // printf("leng1=%d\n", sizeof(str) - 1);
    // bool b = isValid(str);
    // printf("bool=%d\n", b);
    return 0;
}