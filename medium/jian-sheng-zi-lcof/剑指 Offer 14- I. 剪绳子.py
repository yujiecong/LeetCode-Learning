class Solution:
    def cuttingRope(self, n: int) -> int:
        l=n #用 l来作为绳子长度
        dp=[0]*(l+1)
        dp[2]=1
        for i in range(3,l+1):
            for j in range(2,i//2+2):
                # print(dp[j],dp[i-j])
                # print(i,j)
                dp[i]=(max(dp[i],max(j*(i-j),j*dp[i-j])))

        return dp[l]

Solution().cuttingRope(3)