class Solution:
    def countAndSay(self, n: int) -> str:
        string='1'

        for _ in range(n-1):
            leng = 0
            target = string[0]
            say = ''
            for i in range(len(string)):
                if(string[i]==target):
                    leng+=1
                if(i<len(string)-1):
                    if(string[i+1]!=target):
                        say+=str(leng)+target
                        target = string[i+1]
                        leng=0
            say+=str(leng)+target
            string=say
        return string
    #方法2
    # def countAndSay(self, n: int) -> str:
    #     if (n==1):
    #         return '1'
    #     else:
    #         return self.description('1',n-1)
    # def description(self,string,n):
    #     if (n>0):
    #         leng = 0
    #         target = string[0]
    #         say = ''
    #         for i in range(len(string)):
    #             if (string[i] == target):
    #                 leng += 1
    #             if (i < len(string) - 1):
    #                 if (string[i + 1] != target):
    #                     say += str(leng) + target
    #                     target = string[i + 1]
    #                     leng = 0
    #         say += str(leng) + target
    #         string = say
    #         n -= 1
    #         return self.description(string,n)
    #     else:
    #         return string


s=Solution()
print(s.countAndSay(6))






