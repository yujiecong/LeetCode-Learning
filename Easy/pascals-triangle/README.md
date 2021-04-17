# [118. 杨辉三角](https://leetcode-cn.com/problems/pascals-triangle/)

给定一个非负整数 *numRows，*生成杨辉三角的前 *numRows* 行。

![img](img/PascalTriangleAnimated2.gif)

在杨辉三角中，每个数是它左上方和右上方的数的和。

**示例:**

```
输入: 5
输出:
[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]
```

## 个人见解

这题大家都会蛮熟悉的,就不说了,直接干就完了

当n=0时返回[]

当n=1时返回[1]

当n>=2时开始让首位都为0

当n>=3时,开始保存上一排的数据,然后用lastros[i-1] lastrow[i+1]的方式获得当前row的值

```python 
class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        rowList=[[1],[1,1]]
        if(numRows==0):
            return []
        if(numRows==1):
            return rowList[:1]
        elif(numRows==2):
            return rowList[:2]
        elif(numRows>=3):
            for row in range(1,numRows-1):
                templist = [1,1]
                lastrow=rowList[row]
                for colunm in range(1,len(lastrow)):
                    templist.insert(colunm,lastrow[colunm-1]+lastrow[colunm])
                rowList.append(templist)
        return rowList
```

![1604220477669](img/1604220477669.png)

当然这里优化空间有点多,用的是复杂度很高的insert操作

不过即使换成append也是一样的

过!

```python
            for row in range(1,numRows-1):
                templist = [1]
                lastrow=rowList[row]
                for colunm in range(1,len(lastrow)):
                    templist.append(lastrow[colunm-1]+lastrow[colunm])
                templist+=[1]
                rowList.append(templist)
```

