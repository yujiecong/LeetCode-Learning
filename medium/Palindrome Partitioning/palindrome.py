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
