class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        strin=str(x)
        newstrin=""
        num=0
        if x<0:
            x*=-1
            strin=str(x)
            newstrin+=strin[::-1]
            num-=int(newstrin)
        else:
            strin=str(x)
            newstrin+=strin[::-1]
            num+=int(newstrin)
        if num>(2**31) or num < -(2**31):
            return 0
        else:
            return num
        
        