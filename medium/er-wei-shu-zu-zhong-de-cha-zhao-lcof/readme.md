#### [剑指 Offer 04. 二维数组中的查找](https://leetcode-cn.com/problems/er-wei-shu-zu-zhong-de-cha-zhao-lcof/)

在一个 n * m 的二维数组中，每一行都按照从左到右递增的顺序排序，每一列都按照从上到下递增的顺序排序。请完成一个高效的函数，输入这样的一个二维数组和一个整数，判断数组中是否含有该整数。

 

**示例:**

现有矩阵 matrix 如下：

```
[
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]
```

给定 target = `5`，返回 `true`。

给定 target = `20`，返回 `false`。

 

**限制：**

```
0 <= n <= 1000
0 <= m <= 1000
```



这题实际上是观察规律的题



由于是从上到下递增,从 左到右递增,我们随便找一个数试试就知道

如果target 是 5

那么肯定是从右上角找起来

即 比较 5<15 难么 在他的左边

5<11 在左边

5<7 在左边

4<5 在下面

5=5 查找完成

所以大概的流程就是这样

如果没找到的话就是,最后的索引等于 (0,n)

```
class Solution:
    def findNumberIn2DArray(self, matrix, target: int) -> bool:
        if not matrix:
            return False
        n,m=len(matrix),len(matrix[0])
        if m==0:
            return False
        row,col=0,m-1

        while 1:
            ## print(row,col)
            cur=matrix[row][col]
            # print(cur,target)
            if target== cur:
                return True
            if target<cur:
                col-=1
            else:
                row+=1
            if row>=n or col<0:
                break
        return False
```

![1618118326737](README.assets/1618118326737.png)