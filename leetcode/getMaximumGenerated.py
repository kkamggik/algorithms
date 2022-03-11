class Solution(object):
    def getMaximumGenerated(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [0]*(101)
        dp[1] = 1
        for i in range(2,n+1):
            if i%2==0:
                dp[i] = dp[i//2]
            else:
                dp[i] = dp[i//2]+dp[(i//2)+1]
        return max(dp[:n+1])