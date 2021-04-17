class Solution:
    def searchInsert(self, nums: list, target: int) -> int:
        if target in nums:
            return nums.index(target)
        else:
            t=[i+1 for i in range(len(nums)-1,-1,-1) if target > nums[i]]
            if (t!=[]):
                return t[0]
            else:
                return 0