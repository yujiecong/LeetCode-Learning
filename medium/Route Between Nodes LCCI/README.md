#### [面试题 04.01. Route Between Nodes LCCI](https://leetcode-cn.com/problems/route-between-nodes-lcci/)

Given a directed graph, design an algorithm to find out whether there is a route between two nodes.

**Example1:**

```
 Input: n = 3, graph = [[0, 1], [0, 2], [1, 2], [1, 2]], start = 0, target = 2
 Output: true
```

**Example2:**

```
 Input: n = 5, graph = [[0, 1], [0, 2], [0, 4], [0, 4], [0, 1], [1, 3], [1, 4], [1, 3], [2, 3], [3, 4]], start = 0, target = 4
 Output true
```

**Note:** 

1. `0 <= n <= 100000`
2. All node numbers are within the range [0, n].
3. There might be self cycles and duplicated edges.

有向图寻找路径的话, bfs 和dfs 都上一次 试试

根据我所学的找路径,是用队列做的

python里队列 在 collections 的 queue 双向队列



这个其实就是邻接表的bfs实现 跟以前直接寻找迷宫出口是不太一样的,因为这里直接给的是任意一点到一点的路径存不存在.

查看过的结点用set保存 不要用 列表 和in了

```
import collections
class Solution:
    def findWhetherExistsPath(self, n: int, graph, start: int, target: int) -> bool:
        # 记录所有的边
        edges = [[] for i in range(n)]
        for i, j in graph:
            edges[i].append(j)
        queue = collections.deque()
        queue.append(start)#开始结点
        visited = set()#用一个集合判断当前是否走过
        while queue: #当还有路径要走
            length = len(queue) #查看当前结点还能走去哪(路的边数
            for _ in range(length):
                i = queue.popleft() #出队
                visited.add(i) # 将当前结点加入
                if i == target: # 如果 当前是target
                    return True
                for j in edges[i]: #对于当前结点能走的地方遍历
                    if j not in visited#将 邻接表记录下去
                        queue.append(j)
        return False

```

其实是复制粘贴的.唉

[https://leetcode-cn.com/problems/route-between-nodes-lcci/solution/python3-bfsjie-fa-by-lienlei-efky/](https://leetcode-cn.com/problems/route-between-nodes-lcci/solution/python3-bfsjie-fa-by-lienlei-efky/)

