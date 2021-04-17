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
