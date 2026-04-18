class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        list1=[-1,-1]
        for i in range(len(nums)):
            if (nums[i] == target) and list1[0]== -1:
                list1[0]=i
            if (nums[-1-i] == target) and list1[1]== -1:
                list1[1]=len(nums)-i-1
        return list1
