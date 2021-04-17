#### [77. 组合](https://leetcode-cn.com/problems/combinations/)

给定两个整数 *n* 和 *k*，返回 1 ... *n* 中所有可能的 *k* 个数的组合。

**示例:**

```
输入: n = 4, k = 2
输出:
[
  [2,4],
  [3,4],
  [2,3],
  [1,2],
  [1,3],
  [1,4],
]
```

很容易看出是一个 k 层的for 循环

但是 当k大时就很蠢 复杂度很高,所以我们应该用回溯的思想 遍历 

```
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res=[]
        def backt(i,tmp):
            if len(tmp)==k:
                res.append(tmp)
                return
            for j in range(i,n+1):
                backt(j+1,tmp+[j])
        backt(1,[])
        return res
```

![1618633183578](readme.assets/1618633183578.png)

这里值得一提的是  可以像上面这样用临时的 数组来 替代回溯的步骤 也可以像这样 比较有代表性

```
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:

        ##先生成数
        nums = [i for i in range(1,n+1)]
        # print(nums)

        ##明显用回溯法:
        res = []

        def backtrace(nums_b,curr_res,index):
            # print("curr_res:",curr_res)
            if len(curr_res)==k:
                res.append(curr_res[:]) ##浅拷贝，这一步很重要
                return 

            for i in range(index,n):
                # print(i,nums_b)
                curr_res.append(nums[i])
                backtrace(nums_b[index:],curr_res,i+1)
                curr_res.pop()

        ##特殊情况处理
        if n==0 or k==0:
            return res

        backtrace(nums,[],0)
        return res




作者：zhengvh
链接：https://leetcode-cn.com/problems/combinations/solution/python-jian-dan-de-hui-su-fa-by-zhengvh/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
```

