class Solution:
    def exchange(self,nums) :
        if not nums:
            return []
        i,j=0,len(nums)-1

        while i!=j:
            #从右边开始找起,直到找到一个奇数
            while j>0 and nums[j]&0x1!=0  :
                j-=1
            #从左边开始找齐,直到偶数 或者到尽头
            while i<len(nums) and nums[i]&0x1==0  :
                i+=1
            if i>j:
                break
            nums[i],nums[j]=nums[j],nums[i]
        return nums
print(Solution().exchange([1,11,14]))