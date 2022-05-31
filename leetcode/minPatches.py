class Solution(object):
    def minPatches(self, nums, n):
        """
        :type nums: List[int]
        :type n: int
        :rtype: int
        """
        t = 1
        idx = res = 0
        while t <= n:
            if idx < len(nums) and nums[idx] <= t:
                t += nums[idx]
                idx += 1
            else:
                t += t
                res += 1
        return res