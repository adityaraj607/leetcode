class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        st=""
        while num!=0:
            if num>=1000:
                st+="M"
                num-=1000
            elif num>=900:
                st+="CM"
                num-=900
            elif num>=500:
                st+="D"
                num-=500
            elif num>=400:
                st+="CD"
                num-=400
            elif num>=100:
                st+="C"
                num-=100
            elif num>=90:
                st+="XC"
                num-=90
            elif num>=50:
                st+="L"
                num-=50
            elif num>=40:
                st+="XL"
                num-=40
            elif num>=10:
                st+="X"
                num-=10
            elif num>=9:
                st+="IX"
                num-=9
            elif num>=5:
                st+="V"
                num-=5
            elif num>=4:
                st+="IV"
                num-=4
            elif num>=1:
                st+="I"
                num-=1
        return st