class Solution(object):
    def numSubarrayProductLessThanK(self, nums, k):
        if k <= 1:
            return 0
        mul = 1
        res = 0
        left = 0
        for right, val in enumerate(nums):
            mul *= val
            while mul >= k:
                mul /= nums[left]
                left += 1
            res += right - left + 1
        return res
