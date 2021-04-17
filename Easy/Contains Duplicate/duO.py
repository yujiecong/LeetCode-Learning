class Solution:
    def containsDuplicate(self, nums:list) -> bool:
        if len(nums)<=1:
            return False
        d={}
        for ele in nums:
            if ele not in d:
                d[ele]=1
            else:
                return True
        return False
print(Solution().containsDuplicate([1,2,3,4]))