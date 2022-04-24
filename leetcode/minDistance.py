class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        # longestCommonSubsequent 구해서 계산
        n,m = len(word1), len(word2)
        dp = [[0]*(n+1) for _ in range(m+1)]
        for i in range(1,m+1):
            for j in range(1,n+1):
                if word1[j-1]==word2[i-1]: dp[i][j] = 1 + dp[i-1][j-1]
                else: dp[i][j] = max(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])
        return n+m-2*dp[m][n]
                
        