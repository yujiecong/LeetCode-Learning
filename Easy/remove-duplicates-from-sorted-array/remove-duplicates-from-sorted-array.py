class Solution:
    def removeDuplicates(self, nums) -> int:
        """
        :type nums: List[int]
        :rtype: int
        """
        arr=list()
        for num in nums:
            if(nums.count(num)==1):
                arr.append(num)
            else:
                for i in range(0,nums.count(num)-1):
                    nums.remove(num)
        print(nums)
        return len(nums)

s=Solution()
print(s.removeDuplicates([1,1,1,1]))