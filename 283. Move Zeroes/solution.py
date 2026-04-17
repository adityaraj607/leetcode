class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        newnums=[]
        allzeros=[]
        for i in nums:
            if i == 0:
                allzeros.append(0)
            else:
                newnums.append(i)
        nums[:]=newnums+allzeros
