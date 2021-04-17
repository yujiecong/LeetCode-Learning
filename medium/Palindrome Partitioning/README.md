#### [131. 分割回文串](https://leetcode-cn.com/problems/palindrome-partitioning/)

给定一个字符串 *s*，将 *s* 分割成一些子串，使每个子串都是回文串。

返回 *s* 所有可能的分割方案。

**示例:**

```
输入: "aab"
输出:
[
  ["aa","b"],
  ["a","a","b"]
]
```



很明显，暴力回溯

找到一个舒服的模板

> res = []
> path = []
>
> def backtrack(未探索区域, res, path):
>     if 未探索区域满足结束条件:
>         res.add(path) # 深度拷贝
>         return
>     for 选择 in 未探索区域当前可能的选择:
>         if 当前选择符合要求:
>             path.add(当前选择)
>             backtrack(新的未探索区域, res, path)
>             path.pop()
>
> 作者：fuxuemingzhu
> 链接：https://leetcode-cn.com/problems/palindrome-partitioning/solution/hui-su-fa-si-lu-yu-mo-ban-by-fuxuemingzh-azhz/
> 来源：力扣（LeetCode）
> 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

我们简单写一个递归

注意是自下而上的基于增量的回溯，简单明了

用匿名函数注册一个判断回文，可读性增强

```
class Solution(object):
    def partition(self, s):
        self.isPalindrome = lambda s : s == s[::-1]
        res = []
        self.backtrack(s, res, [])
        return res
        
    def backtrack(self, s, res, path):
        print(path)
        if not s: #如果是空字符串 ''
            res.append(path)
            return
        for i in range(1, len(s) + 1): #注意起始和结束位置
            if self.isPalindrome(s[:i]):#如果符合回文
                self.backtrack(s[i:], res, path + [s[:i]])

Solution().partition("aab")

```



![1615087204548](img/1615087204548.png)