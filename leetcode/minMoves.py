class Solution(object):
    def minMoves(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = 0 
        m = min(nums)
        for n in nums:
            res += abs(n-m)
        return res
        