class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        dp = [[False] * n for _ in range(n)]
        ans = ""
        # 枚举子串的长度 l+1
        for l in range(n):
            # 枚举子串的起始位置 i，这样可以通过 j=i+l 得到子串的结束位置
            for i in range(n):
                j = i + l
                # print(s[i:j]) s[i:j]就是所有的子串
                if j >= len(s): # 当 子串的长度大于等于s的长度时 也就是说 子串尾指针 到头了 直接break
                    break
                if l == 0: # 第一个字符作为子串 肯定是 回文
                    dp[i][j] = True
                elif l == 1: # 子串长度为2 作为回文，那肯定是两个相等才是回文的
                    dp[i][j] = (s[i] == s[j])
                else: #如果子串长度为>2 那么就要穷举逐个判断了
                    dp[i][j] = (dp[i + 1][j - 1] and s[i] == s[j])
                if dp[i][j] and l + 1 > len(ans): # 如果第 i 到 j的 子串是回文并且 长度比之前的子串长的话
                    ans = s[i:j + 1]
        return ans
Solution().longestPalindrome("aabb")
