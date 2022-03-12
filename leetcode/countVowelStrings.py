class Solution(object):
    def countVowelStrings(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [[0]*5 for _ in range(n+1)]
        for i in range(5):
            dp[0][i] = 1
        for j in range(n+1):
            dp[j][4] = 1
        for i in range(1,n+1):
            for j in range(3,-1,-1):
                dp[i][j] = dp[i-1][j] + dp[i][j+1]
        return dp[n][0]