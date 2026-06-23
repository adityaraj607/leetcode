class Solution(object):
    def sortArrayByParityII(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        odd=[]
        even=[]
        final=[]
        for i in nums:
            if i%2==0:
                even.append(i)
            else:
                odd.append(i)
        for i in range(len(nums)):
            if i%2==0:
                final.append(even[-1])
                even.pop()
            else:
                final.append(odd[-1])
                odd.pop()
        return final
