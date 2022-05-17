class Solution(object):
    def gridGame(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        n = len(grid[0])
        t = sum(grid[0])
        b = 0
        res = math.inf
        for i in range(n):
            t -= grid[0][i]
            res = min(res, max(t,b))
            b += grid[1][i]
        return res