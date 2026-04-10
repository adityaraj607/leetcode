class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        s=""
        for i in digits:
            s+=str(i)
        num=int(s)
        num+=1
        s=str(num)
        list1=[]
        for i in s:
            list1.append(int(i))
        return list1