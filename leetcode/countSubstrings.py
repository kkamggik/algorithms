class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        dp = [[0]*n for _ in range(n)]
        for i in range(n):
            dp[i][i] = 1
        res = n
        for i in range(n-1):
            if s[i]==s[i+1]:
                res += 1
                dp[i][i+1] = 1
        for k in range(3,n+1):
            for i in range(n-k+1):
                j = i+k-1
                if s[i]==s[j] and dp[i+1][j-1]:
                    dp[i][j] = 1
                    res += 1
        return res
