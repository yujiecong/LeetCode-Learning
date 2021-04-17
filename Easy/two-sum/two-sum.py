class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numLeng=len(nums)
        for i in range(0,numLeng-1):
            for j in range(i+1,numLeng):
                if(nums[i]+nums[j]==target):
                    return [i,j]
s=Solution()
s.twoSum([3,2,4],6)