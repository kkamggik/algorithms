class Solution(object):
    def champagneTower(self, poured, query_row, query_glass):
        """
        :type poured: int
        :type query_row: int
        :type query_glass: int
        :rtype: float
        """
        dp = [[0]*101 for _ in range(101)]
        dp[0][0] = poured
        for r in range(query_row):
            for c in range(r+1):
                q = (dp[r][c] - 1.0) / 2.0
                if q > 0:
                    dp[r+1][c] += q
                    dp[r+1][c+1] += q
        return min(1,dp[query_row][query_glass])