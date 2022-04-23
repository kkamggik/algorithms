class Solution(object):
    def findNumberOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dp = [1]*len(nums)
        lng = [1]*len(nums)
        for i in range(1,len(nums)):
            for j in range(i):
                if nums[j] < nums[i]:
                    if dp[i] == dp[j]:
                        dp[i] = dp[j] + 1
                        lng[i] = lng[j]
                    elif dp[i] == dp[j]+1:
                        lng[i] += lng[j]
        m = max(dp)
        res = 0
        for i in range(len(nums)):
            if dp[i]==m:
                res += lng[i]
        return res