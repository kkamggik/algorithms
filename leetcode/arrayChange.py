class Solution(object):
    def arrayChange(self, nums, operations):
        """
        :type nums: List[int]
        :type operations: List[List[int]]
        :rtype: List[int]
        """
        num = {}
        for idx, n in enumerate(nums):
            num[n] = idx
        for a,b in operations:
            idx = num[a]
            num[b] = idx
            nums[idx] = b
        return nums