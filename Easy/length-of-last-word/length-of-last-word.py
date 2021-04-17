class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        # 拿split分割
        arrSplited=s.split(' ')
        #若出现 '' 说明有人搞你，乱搞空格,全部去掉，再看看有木有单词
        while( '' in arrSplited):
            arrSplited.remove('')
        if(not arrSplited):#去掉之后都是空的，那肯定是因为直接输入一堆空格了，就是在搞你
            return 0
        #都来到这里了，肯定有个单词在的了
        leng=len(arrSplited[-1])
        return leng

s=Solution()
print(s.lengthOfLastWord("        "))