class Solution:
    def fib(self, n: int) -> int:
        if n==0:
            return 0
        elif n==1:
            return 1
        fibonacci=[0,1]
        for i in range(2,n+1):
            fibonacci.append((fibonacci[-2]+fibonacci[-1])%1000000007)
            fibonacci.pop(0)
        return fibonacci[-1]

print(Solution().fib(3))