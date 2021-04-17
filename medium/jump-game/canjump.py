class Solution:
    def canJump(self, nums:list) -> bool:
            leng= len(nums);
            longest=0 #一开始最远距离是0
            for i in range(leng):
                if i<=longest: #如果当前能跳的距离小于=最远距离
                    longest=max(longest,i+nums[i])
                    if longest>=leng-1:
                        return True
            return False
            

