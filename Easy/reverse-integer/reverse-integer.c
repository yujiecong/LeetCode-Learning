#include <stdio.h>
long pow_(int p, int n)
{
    if (p == 2 && n == 31)
    {
        return 2147483647;
    }
    int i;
    long result = 1;
    for (i = 0; i < n; i++)
    {
        result *= p;
    }
    return result;
}

int reverse(int x)
{
    int i, arrLeng = 0,signal=1;
    unsigned int r = 0;
    int arr[10];
    int MAX = pow_(2, 31), MIN = -pow_(2, 31) - 1;

    if(x<=MIN || x>MAX){
        return 0;
    }

    if (x < 0)
    {
        x *= -1;
        signal=-1;
    }

    if (x < 10 && x>=0)
    {
        return x > 0 ? x : -x;
    }
    for (i = 0; i < 10; i++)
    {

        arr[i] = x % 10;
        x /= 10;
        arrLeng++;
        
        if (x < 10)
        {
            arr[i + 1] = x % 10;
            arrLeng++;
            break;
        }
    }

    if (arr[0] > 2 && arrLeng == 10)
    {
        return 0;
    }
    else if (arr[0] == 2  && arrLeng == 10)
    {
        int t = MAX - 2000000000;
        for (i = 1; i < arrLeng; i++)
        {
            r += arr[i] * pow_(10, arrLeng - i - 1);
            if (t < r)
                return 0;
        }
        r+=2000000000;
        return signal > 0 ? r : -r;
    }
    for (i = 0; i < arrLeng; i++)
    {
        r += arr[i] * pow_(10, arrLeng - i - 1);
        
    }

    return signal > 0 ? r : -r;
}
int main()
{
    printf("\nr=%d\n", reverse(10));
}
