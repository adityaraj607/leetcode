class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        newnums=set(nums)
        return len(nums)!=len(newnums)
