class Solution:
    def findNumberIn2DArray(self, matrix, target: int) -> bool:
        if not matrix:
            return False
        n,m=len(matrix),len(matrix[0])
        if m==0:
            return False
        row,col=0,m-1

        while 1:
            print(row,col)
            cur=matrix[row][col]
            # print(cur,target)
            if target== cur:
                return True
            if target<cur:
                col-=1
            else:
                row+=1
            if row>=n or col<0:
                break
        return False

print(Solution().findNumberIn2DArray([[-1,3]],-1))