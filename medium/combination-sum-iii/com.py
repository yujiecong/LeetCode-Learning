class Solution:
    def combinationSum3(self, k: int, n: int):
        path=[]
        l=[]
        def dfs(idx,ans):
            if sum(ans)>n:
                return
            if len(path)==k and sum(ans)==n:

                l.append(path[:])
            for i in range(idx,9):

                ans.append(i)
                path.append(i)
                dfs(i+1,ans)
                ans.pop(-1)
                path.pop(-1)
        dfs(1,[])
        print(l)
        return l



Solution().combinationSum3(4,10)