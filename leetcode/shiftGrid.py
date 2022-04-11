class Solution(object):
    def shiftGrid(self, grid, k):
        """
        :type grid: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        n,m = len(grid), len(grid[0])
        queue = deque()
        for i in range(n):
            for j in range(m):
                queue.append(grid[i][j])
        for i in range(k):
            x = queue.pop()
            queue.appendleft(x)
        for i in range(n):
            for j in range(m):
                grid[i][j] = queue.popleft()
        return grid