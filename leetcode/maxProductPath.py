class Solution(object):
    def maxProductPath(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        n,m = len(grid),len(grid[0])
        marr = [[0]*m for _ in range(n)]
        narr = [[0]*m for _ in range(n)]
        marr[0][0] = narr[0][0] = grid[0][0]
        for i in range(1,n):
            marr[i][0] = marr[i-1][0]*grid[i][0]
            narr[i][0] = narr[i-1][0]*grid[i][0]
        for i in range(1,m):
            marr[0][i] = marr[0][i-1]*grid[0][i]
            narr[0][i] = narr[0][i-1]*grid[0][i]
        for i in range(1,n):
            for j in range(1,m):
                if grid[i][j] > 0:
                    marr[i][j] = max(marr[i-1][j],marr[i][j-1])*grid[i][j]
                    narr[i][j] = min(narr[i-1][j],narr[i][j-1])*grid[i][j]
                else:
                    marr[i][j] = min(narr[i-1][j],narr[i][j-1])*grid[i][j]
                    narr[i][j] = max(marr[i-1][j],marr[i][j-1])*grid[i][j]
        res = max(marr[-1][-1],narr[-1][-1])
        return res%(10**9 + 7) if res>=0 else -1