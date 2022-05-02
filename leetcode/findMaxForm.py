class Solution(object):
    def findMaxForm(self, strs, m, n):
        """
        :type strs: List[str]
        :type m: int
        :type n: int
        :rtype: int
        """
        count = [[s.count("0"),s.count("1")] for s in strs]
        dp = [[0]*(n+1) for _ in range(m+1)]
        for zero, one in count:
            for x in range(m, zero-1, -1):
                    for y in range(n, one-1, -1):
                        dp[x][y] = max(1 + dp[x-zero][y-one], dp[x][y])
        return dp[m][n]
