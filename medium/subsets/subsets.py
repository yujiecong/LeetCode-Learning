import itertools
from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        def dfs(begin,path):
            res.append(path[:])
            if begin==len(nums):
                return
            for i in range(begin,len(nums)):
                path.append(nums[i])
                dfs(i+1,path)
                path.pop(-1)
        dfs(0,[])
        print(res)

Solution().subsets([1,2,3])
