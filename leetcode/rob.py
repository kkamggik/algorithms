class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n >= 3:
            dp = [0]*n
            dp[0] = nums[0]
            dp[1] = nums[1]
            dp[2] = max(nums[0]+nums[2], nums[1])
            for i in range(3,n):
                dp[i] = max(dp[i-2], dp[i-3])+nums[i]
        else: return max(nums)
        return max(dp)