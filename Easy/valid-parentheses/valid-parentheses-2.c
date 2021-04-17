char pairs(char a)
{
    if (a == '}')
        return '{';
    if (a == ']')
        return '[';
    if (a == ')')
        return '(';
    return 0;
}

bool isValid(char *s)
{
    int leng = 0;
    for (int i = 0; s[i] != '\0'; i++, leng++)
        ;
    if (leng % 2 == 1)
    {
        return 0;
    }
    int *stk=(int *)malloc(sizeof(int)*leng + 1), top = 0;
    for (int i = 0; i < leng; i++)
    {
        char ch = pairs(s[i]);
        //若是出现了 右括号
        if (ch)
        {
            if (top == 0 || stk[top - 1] != ch)
            {
                return 0;
            }
            top--;
        }
        else
        {
            stk[top++] = s[i];
        }
    }
    return top == 0;
}
