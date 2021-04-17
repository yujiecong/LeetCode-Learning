class Solution(object):
    def reverse(self, x):
        uplimit=2147483647
        downlimit=-2147483648
        x=str(x)
        if (x[0] != '-'):
            x = x[::-1]
            if (int(x) <uplimit and int(x) >downlimit):
                return int(x)
            else:
                return 0
        else:
            x = x[1:][::-1]
            if (int(x) < uplimit and int(x)> downlimit):
                
                return int('-'+x)
            else:
                return 0