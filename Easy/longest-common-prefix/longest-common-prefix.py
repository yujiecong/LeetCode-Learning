class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str

        """
        #首字母
        if (not strs ):
            return ""
        minstr=strs[0]
        if (not minstr):
            return ""
        for str in strs:
           if(len(str)<len(minstr)):
               minstr=str
        flag = 0
        rleng=len(minstr)
        while(flag!=1):

            for str in strs:
                if minstr[:rleng] == str[:rleng]:
                    print(minstr[:rleng] ,str[:rleng])
                    flag=1
                else:
                    flag=0
                    break
            rleng-=1
        if (flag):
            return minstr[:rleng+1]
        else:
            return ''
s=Solution()

print(s.longestCommonPrefix(["reflower","flow","flight"]))