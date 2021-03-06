class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dp = [0]*len(nums)
        m = dp[0] = nums[0]
        for i in range(1,len(nums)):
            if dp[i-1] > 0: dp[i] = dp[i-1]
            dp[i] += nums[i]
        return max(dp)