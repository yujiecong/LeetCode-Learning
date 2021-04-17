class Solution:
    def permute(self, nums):
        ans=[]
        nums.sort()

        def dfs(start):
            if start==len(nums):
                ans.append(nums.copy())
                return
            for i in range(start,len(nums)):
                nums[i],nums[start]=nums[start],nums[i]
                dfs(start+1)
                nums[i],nums[start]=nums[start],nums[i]
        dfs(0)
        print(ans)
        return ans
Solution().permute([1,1,2,2])