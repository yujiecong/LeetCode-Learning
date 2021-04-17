class Solution:
    def findRepeatNumber(self, nums: list[int]) -> int:
        nums.sort()
        t=nums[0]
        for num in nums[1:]:
            if t==num:
                return t
            t=num
