# 直接插入排序
![img](img/1.gif)  

## python实现
其实算法思路也很简单，就是一个比较的关系 ，如果比较不成功，向前移，如果比较成功，则交换。

这里给出两种思路

### 思路1：如上图gif一样交换
```
class Solution:
    #直接插入排序
    def Straight_InsertionSort(self, nums: list) -> int:
        for i in range(1,len(nums)):
            # 从左到右 逐渐遍历
            j=i
            while(j>0):#直到遇见两个相邻变量满足小于关系时交换
                if(nums[j]<nums[j-1]):
                     nums[j - 1], nums[j] = nums[j], nums[j - 1]
                     j = j - 1
                else:
                    break
        return nums
```
### 思路2:向有序数组中插入无序数组
```
    #直接插入一个无序数组到有序数组中
    def Straight_InsertionArray(self,nums,insert):
        for innum in insert:
            for numi in range(len(nums)-1,-1,-1):
                if(innum<nums[0]):
                    nums.insert(0,innum)
                    break
                if(innum>=nums[numi]):
                    nums.insert(numi+1,innum)
                    break
        return  nums
```
以下内容摘录自[https://www.cnblogs.com/jing-an-feng-shao/p/6165094.html](https://www.cnblogs.com/jing-an-feng-shao/p/6165094.html)

> 仔细分析直接插入排序的代码，会发现虽然每次都需要将数组向后移位，但是在此之前的判断却是可以优化的。

> 不难发现，每次都是从有序数组的最后一位开始，向前扫描的，这意味着，如果当前值比有序数组的第一位还要小，那就必须比较有序数组的长度n次。

>这个比较次数，在不影响算法稳定性的情况下，是可以简化的：记录上一次插入的值和位置，与当前插入值比较。若当前值小于上个值，将上个值插入的位置之后的数，全部向后移位，从上个值插入的位置作为比较的起点；反之，仍然从有序数组的最后一位开始比较。

这就比较秒了，这说明，可以跳过很多的步骤了，因为没有必要一个一个从后比到前，只要知道新比较值与就比较值的大小关系，就可以跳过很多了，可能平均是n/2的步骤

以下来自[百度百科](https://baike.baidu.com/item/%E7%9B%B4%E6%8E%A5%E6%8F%92%E5%85%A5%E6%8E%92%E5%BA%8F/8255911?fr=aladdin#2)
> 算法中引进的附加记录R[0]称监视哨或哨兵(Sentinel)。

### 哨兵有两个作用：
#### ① 进入查找(插入位置)循环之前，它保存了R[i]的副本，使不致于因记录后移而丢失R[i]的内容；
#### ② 它的主要作用是：在查找循环中"监视"下标变量j是否越界。一旦越界(即j=0)，因为R[0].可以和自己比较，循环判定条件不成立使得查找循环结束，从而避免了在该循环内的每一次均要检测j是否越界(即省略了循环判定条件"j>=1")。
### 注意：
#### ① 实际上，一切为简化边界条件而引入的附加结点(元素)均可称为哨兵。
- 【例】单链表中的头结点实际上是一个哨兵
#### ② 引入哨兵后使得测试查找循环条件的时间大约减少了一半，所以对于记录数较大的文件节约的时间就相当可观。
对于类似于排序这样使用频率非常高的算法，要尽可能地减少其运行时间。所以不能把上述算法中的哨兵视为雕虫小技，而应该深刻理解并掌握这种技巧。

待更新..
```

```
## C/C++实现
```
#include<iostream>
using namespace std;
int main()
{
    int a[]={98,76,109,34,67,190,80,12,14,89,1};
    int k=sizeof(a)/sizeof(a[0]);
    int i,j;
    for(i=1;i<k;i++)//循环从第2个元素开始
    {
        if(a[i]<a[i-1])
        {
            int temp=a[i];
            for(j=i-1;j>=0 && a[j]>temp;j--)
            {
                a[j+1]=a[j];
            }
            a[j+1]=temp;//此处就是a[j+1]=temp;
        }
    }
    for(int f=0;f<k;f++)
    {
        cout<<a[f]<<"  ";
    }
    return 0;
}
```