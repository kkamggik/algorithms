class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        num = [0]*(n+1)
        for i in nums:
            num[i] = 1
        for i in range(n+1):
            if num[i]==0: return i
        return n