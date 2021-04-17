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
print(Solution().canPlaceFlowers([0,0,0,0],3))
                    
