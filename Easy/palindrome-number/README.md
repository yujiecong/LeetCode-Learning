# [判断一个整数是否是回文数。](https://leetcode-cn.com/problems/palindrome-number)
回文数是指正序（从左向右）和倒序（从右向左）读都是一样的整数。

示例 1:
```
输入: 121
输出: true
```
示例 2:
```
输入: -121
输出: false
```
解释: 从左向右读, 为 -121 。 从右向左读, 为 121- 。因此它不是一个回文数。
示例 3:
```
输入: 10
输出: false
```
解释: 从右向左读, 为 01 。因此它不是一个回文数。
## 进阶:
### 你能不将整数转为字符串来解决这个问题吗？

# 个人解析
## python
这简直了，python为此而生，直接用字符串索引就行了..
```
class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if(str(x)==str(x)[::-1]):
            return True
        else:
            return False
```
## C
c语言则要麻烦一点,得用之前用过的那个方法,即一直除10直到小于10再比较，可以不直接用字符串.
## 思路1:用数组分别存放原来的数和翻转后的数比较
```
#include <stdio.h>
#include <stdlib.h>
#define false 0
#define true 1
typedef int bool;

bool isPalindrome(int x)
{
    
    if (x < 0)
    {
        return false;
    }
    else
    {
        if(x<10){
            return true;
        }
        int leng = 0;
        int t = x;
        while (1)
        {
            t /= 10;
            leng++;
            if (t < 10)
            {
                leng++;
                break;
            }
        }
        // if (x % 10!=0)
        //     leng /= 2;
        //printf("leng=%d \n", leng);
        int *arrInt = (int *)malloc(sizeof(int) * leng);
        int *arrIntReverse = (int *)malloc(sizeof(int) * leng);
        int i;
        for (i = 0; i < leng; i++)
        {
            arrInt[i] = x % 10;
            arrIntReverse[leng - i - 1] = x % 10;
            //printf("arrInt[%d]=%d arrIntReverse[%d]=%d \n", i, arrInt[i], leng - i - 1, arrIntReverse[leng - i ]);

            x /= 10;
        }
        //free
        for (i = 0; i < leng; i++)
        {
            //printf("arrInt[%d]=%d arrIntReverse[%d]=%d \n", i, arrInt[i], leng - i - 1, arrIntReverse[leng-i]);
            if (arrInt[i] != arrIntReverse[i])
            {
                return false;
            }
        }
        return true;
    }
}
int main()
{
    printf("is Palindrome? %d \n", isPalindrome(1));
}
```
这个性能比较低，才达到了这样的性能  
![img](img/1.png)  
算是最低级的了,因为用到了动态数组去存储，浪费了很多空间，接着我们去升级一下   
这个说过了，是根据直觉得到的做法，必然有很多缺陷，我们可以稍微升级一下思路(仅仅是思路..)  
## 思路2:用整数存放原来的数和翻转后的数
```
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
```
![img](img/2.png)  
因为还是好慢a  
不知道怎么回事，先这样了

