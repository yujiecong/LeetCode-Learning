# [28. 实现 strStr](https://leetcode-cn.com/problems/implement-strstr/)
实现 strStr() 函数。

给定一个 haystack 字符串和一个 needle 字符串，在 haystack 字符串中找出 needle 字符串出现的第一个位置 (从0开始)。如果不存在，则返回  -1。

示例 1:
```
输入: haystack = "hello", needle = "ll"
输出: 2
```
示例 2:
```
输入: haystack = "aaaaa", needle = "bba"
输出: -1
```
说明:

当 needle 是空字符串时，我们应当返回什么值呢？这是一个在面试中很好的问题。

对于本题而言，当 needle 是空字符串时我们应当返回 0 。这与C语言的 strstr() 以及 Java的 indexOf() 定义相符。

通过次数247,621提交次数624,523

## 个人见解
### python
这题..
```
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        return haystack.find(needle)
```
...

![img](img/py.png)

...
除了这种方法，当然还有所谓的，也就是，比较容易想出来的
### [滑动窗口](https://leetcode-cn.com/problems/implement-strstr/solution/shi-xian-strstr-by-leetcode/)
即把整个needle当做一个整体，整体遍历haystack，即可
```
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        L, n = len(needle), len(haystack)

        for start in range(n - L + 1):
            if haystack[start: start + L] == needle:
                return start
        return -1

```

复杂度分析

时间复杂度：O((N - L)L)O((N−L)L)，其中 N 为 haystack 字符串的长度，L 为 needle 字符串的长度。内循环中比较字符串的复杂度为 L，总共需要比较 (N - L) 次。

空间复杂度：O(1)O(1)。

当然还有一种方法，双指针，也很容易想到
### [双指针](https://leetcode-cn.com/problems/implement-strstr/solution/shi-xian-strstr-by-leetcode/)
当然具体就去参考答案看了