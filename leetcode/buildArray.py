class Solution(object):
    def buildArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        new = [0]*n
        for i in range(n):
            new[i] = nums[nums[i]]
        return new