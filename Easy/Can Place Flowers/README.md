#### [605. 种花问题](https://leetcode-cn.com/problems/can-place-flowers/)

假设有一个很长的花坛，一部分地块种植了花，另一部分却没有。可是，花不能种植在相邻的地块上，它们会争夺水源，两者都会死去。

给你一个整数数组 `flowerbed` 表示花坛，由若干 `0` 和 `1` 组成，其中 `0` 表示没种植花，`1` 表示种植了花。另有一个数 `n` ，能否在不打破种植规则的情况下种入 `n` 朵花？能则返回 `true` ，不能则返回 `false`。

 

**示例 1：**

```
输入：flowerbed = [1,0,0,0,1], n = 1
输出：true
```

**示例 2：**

```
输入：flowerbed = [1,0,0,0,1], n = 2
输出：false
```

 

**提示：**

- `1 <= flowerbed.length <= 2 * 104`
- `flowerbed[i]` 为 `0` 或 `1`
- `flowerbed` 中不存在相邻的两朵花
- `0 <= n <= flowerbed.length`

通过次数79,933提交次数

专门练习贪心算法了，感觉不是很适应，所以来适应一下

其实跟状态转移方程挺像 的额，但是我一般都是靠感觉来的

这里考虑极限情况，flowerbed是空时和小于3时 

这个时候由于n>=1 也就是 无论怎么样种植都是不行的，直接返回

然后开始遍历，用一个检测来表示

要注意的是，有很多边界条件要考虑，这就是我错了这么多次的原因



![1614786623099](img/1614786623099.png)

```
class Solution:
    def canPlaceFlowers(self, flowerbed, n: int) -> bool:
        if not flowerbed:
            return False
        elif n==0:
            return True
        elif len(flowerbed)==1:
            if n==1:
                return True if flowerbed[0]==0 else False
            else:
                return False
        else:
            
            i=0
            if len(flowerbed)>=3:
                if flowerbed[0]==0 and flowerbed[1]==0:
                    n-=1
                    i+=2
                if flowerbed[-1]==0 and flowerbed[-2]==0:
                    n-=1
                    flowerbed[-1]=1
                    
            while i<len(flowerbed)-1:
                if flowerbed[i]==0 :
                    if flowerbed[i+1]==0 and flowerbed[i-1]==0:
                        n-=1
                        flowerbed[i]=1
                        i+=1

                i+=1
        return n<=0
```

![1614786662660](img/1614786662660.png)