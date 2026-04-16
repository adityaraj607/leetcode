class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        freq={}
        for i in nums:
            if i in freq:
                freq[i]+=1
            else:
                freq[i]=1
        maxk=0
        maxv=0
        for i in freq:
            if freq[i]>maxv:
                maxk=i
                maxv=freq[i]
        return maxk
