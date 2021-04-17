def trackBack():
    pass


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

print(Solution().movingCount(16, 8, 0))
