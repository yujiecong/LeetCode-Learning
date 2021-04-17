class Solution:
    def maxSubArray(self, nums) -> int:
        tmp = nums[0]
        max_ = tmp
        n = len(nums)
        for i in range(1, n):
            print("tmp={} max_={}".format(tmp,max_))
            # 当当前序列加上此时的元素的值大于tmp的值，说明最大序列和可能出现在后续序列中，记录此时的最大值
            print("tmp + nums[i] ={} + {} = {}".format(tmp, nums[i], tmp + nums[i]))
            if tmp + nums[i] > nums[i]:

                max_ = max(max_, tmp + nums[i])
                tmp = tmp + nums[i]
            else:
                # 当tmp(当前和)小于下一个元素时，当前最长序列到此为止。以该元素为起点继续找最大子序列,
                # 并记录此时的最大值
                max_ = max(max_, tmp, tmp + nums[i], nums[i])
                tmp = nums[i]
        return max_
