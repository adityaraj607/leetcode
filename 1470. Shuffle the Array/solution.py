class Solution(object):
    def shuffle(self, nums, n):
        """
        :type nums: List[int]
        :type n: int
        :rtype: List[int]
        """
        newlist=[]
        for i in range(n):
            newlist.append(nums[i])
            newlist.append(nums[i+n])
        return newlist
        