class Solution(object):
    def minPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        a=0
        for i in range(len(nums)):
            a=max(a,nums[i]+nums[-1-i])
        return a
