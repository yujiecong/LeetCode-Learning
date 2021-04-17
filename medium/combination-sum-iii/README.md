#### [216. 组合总和 III](https://leetcode-cn.com/problems/combination-sum-iii/)

找出所有相加之和为 ***n*** 的 ***k\*** 个数的组合***。\***组合中只允许含有 1 - 9 的正整数，并且每种组合中不存在重复的数字。

**说明：**

- 所有数字都是正整数。
- 解集不能包含重复的组合。 

**示例 1:**

```
输入: k = 3, n = 7
输出: [[1,2,4]]
```

**示例 2:**

```
输入: k = 3, n = 9
输出: [[1,2,6], [1,3,5], [2,3,4]]
```

看到这种题,很显然的方法是一个暴力的方法,那么n的最大值肯定是 1+2+3+4..+9

只要回溯一下

```
class Solution:
    def combinationSum3(self, k: int, n: int):
        path=[]
        l=[]
        def dfs(idx,ans):
            if sum(ans)>n:
                return
            if len(path)==k and sum(ans)==n:
                l.append(path[:]) # deepcopy
            for i in range(idx,9):

                ans.append(i)
                path.append(i)
                dfs(i+1,ans)
                ans.pop(-1)
                path.pop(-1)
        dfs(1,[])
        print(l)
        return l



Solution().combinationSum3(4,10)
```

![1618110262166](README.assets/1618110262166.png)