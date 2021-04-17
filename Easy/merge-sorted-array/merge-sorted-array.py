class Solution:
    def merge(self, nums1, m: int, nums2, n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        nums1leng=len(nums1)
        for i in range(m,nums1leng):
            nums1[i]=nums2[i-m]
        nums1.sort()
        return nums1
        # return nums1
s=Solution()
print(s.merge([1,2,0,0],2,[1,2],2))






