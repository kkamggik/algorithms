class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        n,m = len(grid), len(grid[0])
        for i in range(n):
            for j in range(m):
                if i==0 and j==0: continue
                if i==0:
                    grid[i][j] += grid[i][j-1]
                elif j==0:
                    grid[i][j] += grid[i-1][j]
                else:
                    grid[i][j] += min(grid[i-1][j], grid[i][j-1])
        return grid[n-1][m-1]