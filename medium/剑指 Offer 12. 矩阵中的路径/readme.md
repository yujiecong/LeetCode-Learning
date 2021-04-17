#### [剑指 Offer 12. 矩阵中的路径](https://leetcode-cn.com/problems/ju-zhen-zhong-de-lu-jing-lcof/)

给定一个 `m x n` 二维字符网格 `board` 和一个字符串单词 `word` 。如果 `word` 存在于网格中，返回 `true` ；否则，返回 `false` 。

单词必须按照字母顺序，通过相邻的单元格内的字母构成，其中“相邻”单元格是那些水平相邻或垂直相邻的单元格。同一个单元格内的字母不允许被重复使用。

 

例如，在下面的 3×4 的矩阵中包含单词 "ABCCED"（单词中的字母已标出）。

![img](readme.assets/word2.jpg)

 

**示例 1：**

```
输入：board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
输出：true
```

**示例 2：**

```
输入：board = [["a","b"],["c","d"]], word = "abcd"
输出：false
```

这是就知道一眼 就知道是dfs 了

老规矩了

先设一个方向变量

嗯..发现这又要是一个回溯的操作,得遍历所有可能再带进去的话,有点想是那个括号那一题了

```
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
```

