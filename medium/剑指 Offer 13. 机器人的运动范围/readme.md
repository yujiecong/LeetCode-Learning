#### [剑指 Offer 13. 机器人的运动范围](https://leetcode-cn.com/problems/ji-qi-ren-de-yun-dong-fan-wei-lcof/)

地上有一个m行n列的方格，从坐标 `[0,0]` 到坐标 `[m-1,n-1]` 。一个机器人从坐标 `[0, 0] `的格子开始移动，它每次可以向左、右、上、下移动一格（不能移动到方格外），也不能进入行坐标和列坐标的数位之和大于k的格子。例如，当k为18时，机器人能够进入方格 [35, 37] ，因为3+5+3+7=18。但它不能进入方格 [35, 38]，因为3+5+3+8=19。请问该机器人能够到达多少个格子？

 

**示例 1：**

```
输入：m = 2, n = 3, k = 1
输出：3
```

**示例 2：**

```
输入：m = 3, n = 1, k = 0
输出：1
```

**提示：**

- `1 <= n,m <= 100`
- `0 <= k <= 20`

相信一开始很多人都是直接遍历二维矩阵 来 判断的.可惜这个是不连通的,你从0,0 走不到一些地方,有障碍物

所以哈哈哈

只能搜索路径了

由于是从0,0 开始走,那么每一次用vis 判断是否走过,然后加1 这些都是很熟悉的了

```
class Solution:
    def movingCount(self, m: int, n: int, k: int) -> int:
        def isVaild(m, n):
            if sum(map(int, list(str(m) + str(n)))) <= k:
                # print(m,n,k)
                return True
            return False

        vis = set()
        print(m,n,k)
        def dfs(row, col):
            if row >= m or row < 0 or col >= n or col < 0 or (row, col) in vis:
                return 0
            if isVaild(row, col):
                vis.add((row, col))
                res = 1 + dfs(row + 1, col) + dfs(row - 1, col) + dfs(row, col + 1) + dfs(row, col - 1)
                return res
            return 0

        return dfs(0, 0)
```

值得注意的是, 这里并不需要回溯状态,因为 返回0 就代表着这条路走不通,不会对目前状态产生影响

![1618287030855](readme.assets/1618287030855.png)

其实最重要的是研究一下

```
res = 1 + dfs(row + 1, col) + dfs(row - 1, col) + dfs(row, col + 1) + dfs(row, col - 1)
```

这个的意思

直观上的意思很显然就是 等于当前地方可以走(那个1)  加上 下面那个格子 能走的路径 ? 加上 上面那个格子能走的路径 加上 .. 的路径 但是如果你将他拆开理解(迭代后) 就会发现有些抽象 

嗯..

我要说的就这么多

还有一种是bfs的解法,这个我也熟悉一下

```
class Solution:
    def movingCount(self, m: int, n: int, k: int) -> int:
        visited = [[1] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if i // 10 + i % 10 + j // 10 + j % 10 <= k:
                    visited[i][j] = 0

        queue = collections.deque([(0, 0)])
        res = 0
        #当队列中还有路可以走时
        while queue:
        	# x,y 出队 看看能不能走下一步
            x, y = queue.popleft()
            res += 1 #当前格子 可以走 就+1
            for dx, dy in ((1, 0), (0, 1)):
                nx, ny = x + dx, y + dy # 下一步走哪?
                #如果可以走 并且没来过
                if 0 <= nx < m and 0 <= ny < n and not visited[nx][ny]:
                    visited[nx][ny] = 1
                    queue.append((nx, ny))
        return res


作者：edelweisskoko
链接：https://leetcode-cn.com/problems/ji-qi-ren-de-yun-dong-fan-wei-lcof/solution/jian-zhi-offer-13-ji-qi-ren-de-yun-dong-wvyll/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
```

