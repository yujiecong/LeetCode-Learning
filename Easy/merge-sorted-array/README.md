# [88. 合并两个有序数组](https://leetcode-cn.com/problems/merge-sorted-array/)

给你两个有序整数数组 *nums1* 和 *nums2*，请你将 *nums2* 合并到 *nums1* 中*，*使 *nums1* 成为一个有序数组。



**说明：**

- 初始化 *nums1* 和 *nums2* 的元素数量分别为 *m* 和 *n* 。
- 你可以假设 *nums1* 有足够的空间（空间大小大于或等于 *m + n*）来保存 *nums2* 中的元素。

 

**示例：**

```
输入：
nums1 = [1,2,3,0,0,0], m = 3
nums2 = [2,5,6],       n = 3

输出：[1,2,2,3,5,6]
```

 

**提示：**

- `-10^9 <= nums1[i], nums2[i] <= 10^9`
- `nums1.length == m + n`
- `nums2.length == n`

## 个人见解

很明显的排序题，有多种解法思路

### python

#### 思路1 整合重排

由于是将nums1**原地**修改，所以我们需要把nums2数组赋值进去

```python
        nums1leng=len(nums1)
        for i in range(m,nums1leng):
            nums1[i]=nums2[i-m]
```

接着由于是**原地修改**，不能直接sorted返回，需要用列表自带的sort实现

```python
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
```

![1603864711359](img/1603864711359.png)

#### 思路2 直接插入

这里稍微提及了一下 [Straight-Insertion-Sort](..\..\Sort-Algorithm\Straight-Insertion-Sort) 
大意是直接插入，不过复杂度还高一点，就没必要提及了
