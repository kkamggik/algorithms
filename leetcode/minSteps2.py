class Solution(object):
    def minSteps(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [1e9]*1001
        dp[1] = 0
        dp[2] = 2
        for i in range(3,n+1):
            for j in range(1,i):
                # if it is divisible by j
                if(i-j) % j == 0:
                    # dp[j] + copy + # of paste
                    dp[i] = min(dp[i], dp[j] + 1 + (i-j)//j)
        return dp[n]
            
        