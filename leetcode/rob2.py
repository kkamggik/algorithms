class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def rob(nums):
            dp = [0]*len(nums)
            dp[0] = nums[0]
            dp[1] = max(nums[0], nums[1])
            for i in range(2, len(nums)):
                dp[i] = max(dp[i-1], dp[i-2]+nums[i])
            return dp[-1]
        if len(nums)==1: return nums[0]
        elif len(nums)==2: return max(nums[0], nums[1])
        return max(rob(nums[1:]), rob(nums[:-1]))
        