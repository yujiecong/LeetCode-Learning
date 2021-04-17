class Solution:
    def addBinary(self, a: str, b: str) -> str:
        return bin(int(a,2)+int(b,2))[2:]

s=Solution()
print(s.addBinary('11','11'))






