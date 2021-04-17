class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res=[]
        def backt(i,tmp):
            if len(tmp)==k:
                res.append(tmp)
                return
            for j in range(i,n+1):
                backt(j+1,tmp+[j])
        backt(1,[])
        return res