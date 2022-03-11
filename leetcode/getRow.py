class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        dp = [[1]]
        for i in range(1, rowIndex+1):
            arr = [1]
            for j in range(1, len(dp[i-1])):
                arr.append(dp[i-1][j-1]+dp[i-1][j])
            arr.append(1)
            dp.append(arr)
        return dp[rowIndex]
            