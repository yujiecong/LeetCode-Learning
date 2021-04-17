#include <stdio.h>
#include <stdlib.h>
#define false 0
#define true 1
typedef int bool;

bool isPalindrome(int x)
{

    if (x <0 || (x%10==0 && x!=0))
    {
        return false;
    }
    else
    {
        if (x < 10)
        {
            return true;
        }

        int t = 0,num=x;
        while (num>t)
        {

            t = t * 10 + num % 10;
            printf("t=%d num=%d \n",t,num);
            num/= 10;
        }
        
        return num == t || num== t / 10;
    }
    return true;
}
int main()
{
    printf("is Palindrome? %d \n", isPalindrome(121));
}