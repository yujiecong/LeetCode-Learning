#### [51. N 皇后](https://leetcode-cn.com/problems/n-queens/)

**n 皇后问题** 研究的是如何将 `n` 个皇后放置在 `n×n` 的棋盘上，并且使皇后彼此之间不能相互攻击。

给你一个整数 `n` ，返回所有不同的 **n 皇后问题** 的解决方案。

每一种解法包含一个不同的 **n 皇后问题** 的棋子放置方案，该方案中 `'Q'` 和 `'.'` 分别代表了皇后和空位。

 

**示例 1：**

![img](img/queens.jpg)

```
输入：n = 4
输出：[[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]
解释：如上图所示，4 皇后问题存在两个不同的解法。
```

**示例 2：**

```
输入：n = 1
输出：[["Q"]]
```

 

**提示：**

- `1 <= n <= 9`
- 皇后彼此不能相互攻击，也就是说：任何两个皇后都不能处于同一条横行、纵行或斜线上。





这道题我相信小学生都看得懂，也是很经典很经典的题了，那么，应该怎么去想嗯？



直接点的方法就是暴力法，这里有个更好听的名字叫回溯法



## 暴力法

暴力枚举将 N 个皇后放置在 N×N 的棋盘上的所有可能的情况，并对每一种情况判断是否满足皇后彼此之间不相互攻击。 

> 下图来自https://leetcode-cn.com/problems/n-queens/solution/shou-hua-tu-jie-cong-jing-dian-de-nhuang-hou-wen-t/



> ![image.png](img/1599090972-ffZdFD-image.png) 

>  回溯的套路（可硬记）：
>
>     遍历枚举出所有可能的选择。
>     依次尝试这些选择：作出一种选择，并往下递归。
>     如果这个选择产生不出正确的解，要撤销这个选择（将当前的 "Q" 恢复为 "."），回到之前的状态，并作出下一个可用的选择。
>
> 作者：xiao_ben_zhu
> 链接：https://leetcode-cn.com/problems/n-queens/solution/shou-hua-tu-jie-cong-jing-dian-de-nhuang-hou-wen-t/
> 来源：力扣（LeetCode）
> 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。



可以看到，每一个状态都可以细分出很多状态，我们暴力出所有状态后，直接开始判断即可



观察得到每一行和每一列有且仅有一个皇后，那么我们先穷举出来



我初始化一下

```
        l = [["." for _ in range(n)] for _ in range(n)]
```

接着，写递归函数，终止条件是行数=n是很明显的

```
        def nQueen(row):
            if row==n:
                res.append( ["".join(l[i]) for i in range(n)] )
                return
            #遍历每一列，也可以每一行
            for col in range(n):
                if isVaild(row, col):
                    #如果这一行有效直接放一个queen
                    l[row][col] = "Q"
                    #然后在下一个地方继续放
                    nQueen(row + 1)
                    # 当row =3 时来到下面这 
                    #从后面往前面加.
                    #这代表着还原
                    l[row][col] = "."

```

其实难是难在了 判断斜线上，这个规律找死人了

```
        def isVaild(row, col):
            # 判断现在列 有无没有q 
            for i in range(row):
                if l[i][col]== "Q":
                    return False
            #判断左上角斜线
            i,j = row - 1, col - 1
            while i>=0 and j>=0:
                if l[i][j]=="Q":
                    return False
                i,j = i-1,j-1
            # 判断右上角斜线
            i,j = row - 1, col + 1
            while i>=0 and j<n:
                if l[i][j]=="Q":
                    return False
                i,j = i-1,j+1
            return True
```

全部代码是

```
#  Copyright (c) 2021. Lorem ipsum dolor sit amet, consectetur adipiscing elit.
#  Morbi non lorem porttitor neque feugiat blandit. Ut vitae ipsum eget quam lacinia accumsan.
#  Etiam sed turpis ac ipsum condimentum fringilla. Maecenas magna.
#  Proin dapibus sapien vel ante. Aliquam erat volutpat. Pellentesque sagittis ligula eget metus.
#  Vestibulum commodo. Ut rhoncus gravida arcu.



class Solution(object):
    def solveNQueens(self, n):
        # 生成N*N的棋盘，填充棋盘，每个格子默认是“。”表示没有放置皇后
        l = [["." for _ in range(n)] for _ in range(n)]
        print(l)
        res = []
        # 判断当前行有效性
        def isVaild(row, col):
            # 判断现在列 有无没有q
            for i in range(row):
                if l[i][col]== "Q":
                    return False
            #判断左上角斜线
            i,j = row - 1, col - 1
            while i>=0 and j>=0:
                if l[i][j]=="Q":
                    return False
                i,j = i-1,j-1
            # 判断右上角斜线
            i,j = row - 1, col + 1
            while i>=0 and j<n:
                if l[i][j]=="Q":
                    return False
                i,j = i-1,j+1
            return True
        def nQueen(row):
            if row==n:
                res.append( ["".join(l[i]) for i in range(n)] )
                return
            #遍历每一列，也可以每一行
            for col in range(n):
                if isVaild(row, col):
                    #如果这一行有效直接放一个queen
                    l[row][col] = "Q"
                    #然后在下一个地方继续放
                    nQueen(row + 1)
                    # 当row =3 时来到下面这
                    #从后面往前面加.
                    #这代表着还原
                    l[row][col] = "."


        nQueen(0)
        return res
print(Solution().solveNQueens(4))


```



![1614098447313](img/1614098447313.png)



由于借鉴了很多别人的想法，这个算是比较失败的



还有这种全排列，更屌

> https://blog.csdn.net/qq_31910669/article/details/103641497

```
def queen(A, cur=0):
	# 递归回溯思想解决n皇后问题
    if cur == len(A): # 所有的皇后都正确放置完毕，输出每个皇后所在的位置
        print(A)
        return 0
    for col in range(len(A)):
        A[cur], flag = col, True
        for row in range(cur): # 检测本次所放皇后的位置是否在同行同列或同一对角线上
            if A[row] == col or abs(col - A[row]) == cur - row: # 是的话，该位置不能放，向上回溯
                flag = False
                break
        if flag: # 否的话，继续放下一个皇后
            queen(A, cur+1)


n = int(input()) # n为8，就是著名的八皇后问题啦

queen([None] * n)
```

由于8个皇后不能在同一个行，那么任意皇后占据肚子的一行，我们可以定义一个数组，数组第i个数字表示位于第i行的皇后的列号。先把数组的8个数字初始化为0~7 然后对数字进行全排列 即N!种可能



用规律 数组的两个下标 i 和 j 是否有 i-j ==A[j]-b[j] 或者 j-i == A[i]-A[j] 就行



太妙了，这个太妙了，666 太强了