class Solution(object):
    def isMonotonic(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        sortednums=sorted(nums)
        return nums==sortednums or nums==sortednums[::-1]
