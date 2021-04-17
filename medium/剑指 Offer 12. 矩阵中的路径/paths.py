class Solution:
    def exist(self, board, word: str) -> bool:
        direation = ((0, 1), (0, -1), (1, 0), (-1, 0))
        # 方向是 (x,y) 的形式
        # 所以这里是下 上 右 左
        rows = len(board)
        cols = len(board[0])

        def dfs(x, y, idx):
            if idx == len(word):
                return True
            for d in direation:
                tx, ty = x + d[0], y + d[1]
                if 0 <= tx < rows and 0 <= ty < cols and board[tx][ty] == word[idx]:
                    board[tx][ty]="#"
                    if dfs(tx, ty, idx + 1):
                        return True
                    # 这条path不行,要撤回
                    board[tx][ty] = word[idx]
            return False

        for row in range(rows):
            for col in range(cols):
                if board[row][col] == word[0]:
                    board[row][col]="#"
                    if dfs(row, col, 1):
                        return True
                    board[row][col]=word[0]
        return False


# [["A","B","C","E"],["S","F","E","S"],["A","D","E","E"]]
# "ABCESEEEFS"
Solution().exist([["A", "B", "C", "E"], ["S", "F", "E", "S"], ["A", "D", "E", "E"]],
                 "ABCESEEEFS"

                 )
