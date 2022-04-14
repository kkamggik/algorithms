class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        res = 0
        dirc = [[1,0],[-1,0],[0,1],[0,-1]]
        n,m = len(grid), len(grid[0])
        for i in range(n):
            for j in range(m):
                if grid[i][j]==1:
                    res += 4
                    for d in dirc:
                        nx,ny = j+d[0],i+d[1]
                        if 0<=nx<m and 0<=ny<n and grid[ny][nx]==1:
                            res -= 1
        return res
