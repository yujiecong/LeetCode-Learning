#### [面试题 08.01. Three Steps Problem LCCI](https://leetcode-cn.com/problems/three-steps-problem-lcci/)

A child is running up a staircase with n steps and can hop either 1 step, 2 steps, or 3 steps at a time. Implement a method to count how many  possible ways the child can run up the stairs. The result may be large,  so return it modulo 1000000007.

**Example1:**

```
 Input: n = 3 
 Output: 4
```

**Example2:**

```
 Input: n = 5
 Output: 13
```

**Note:**

1. `1 <= n <= 1000000`



简单分析一下，根据dp所学的三部曲来

1、**确定 base case**

2、**确定「状态」，也就是原问题和子问题中会变化的变量**。

3、**确定「选择」，也就是导致「状态」产生变化的行为**。

4、**明确 `dp` 函数/数组的定义**。



### 首先，起始条件是

n=1时 只有一步上楼梯的方式 return 1

n=2 时 只有2 步上楼梯的方式 return 2

n=3 时 有4种，return 4

n=4 时 上楼梯的方式 可以是 f(n-1)+f(n-2) +f(n-3)种方式

### 确定的状态是 小孩的上楼梯的位置

### 确定的选择是 小孩跨一步还是跨两步还是跨三步？

### dp函数 的定义

dp(n) 代表 阶层为n 时的楼梯，小孩一共有多少种走法



所以

容易得到



```
class Solution:
    def waysToStep(self, n: int) -> int:
        if n==1:
            return 1
        elif n==2:
            return 2
        elif n==3:
            return 4
        else:
            l=[1,2,4]
            for i in range(n-3):
                l.append(sum(l)%1000000007)
                l.pop(0)
            print(l)
            return l[-1]
```

![1614511884779](img/1614511884779.png)

