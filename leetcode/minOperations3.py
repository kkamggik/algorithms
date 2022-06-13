class Solution(object):
    def minOperations(self, nums, x):
        """
        :type nums: List[int]
        :type x: int
        :rtype: int
        """
        n = len(nums)
        target = sum(nums) - x
        s = start = 0
        res = 1e9
        for end in range(len(nums)):
            s += nums[end]
            while s > target and start <= end:
                s -= nums[start]
                start += 1
            if s == target:
                res = min(res, n-end-1+start)
        return -1 if res==1e9 else res