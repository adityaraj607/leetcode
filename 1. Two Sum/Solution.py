class Solution(object):
    def twoSum(self, nums, target):
        for i, x in enumerate(nums[:]):
            for y in nums[i+1:]:
                if x + y == target:
                    first_index = nums.index(x)
                    second_index = nums.index(y)

                    if x == y:
                        nums.pop(first_index)
                        second_index = nums.index(y) + 1

                    return first_index, second_index
        return None