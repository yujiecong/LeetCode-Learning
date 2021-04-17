class Solution:
    def myPow(self, x: float, n: int) -> float:
        turn=False
        if n<0:
            turn=True
            n=-n
        if 0<=x<=0.000001:
            return 0
        res=1
        while n:
            if n&1:
                res*=x
            x*=x
            n=n>>1

        return 1/res if turn else res

Solution().myPow(2,-2)