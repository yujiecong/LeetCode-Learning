


class Solution:
    def waysToStep(self, n: int) -> int:
        if n==1:
            return 1
        elif n==2:
            return 2
        elif n==3:
            return 4
        else:
            l=[1,2,4]
            for i in range(n-3):
                l.append(sum(l)%1000000007)
                l.pop(0)
            print(l)
            return l[-1]
Solution().waysToStep(5)