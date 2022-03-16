class Solution(object):
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        queue = deque()
        n,m = len(grid), len(grid[0])
        visited = [[0]*m for _ in range(n)]
        for i in range(n):
            for j in range(m):
                # rotten orange
                if grid[i][j] == 2:
                    queue.append([j,i])
        answer = 0
        dirc = [[1,0],[-1,0],[0,1],[0,-1]]
        while queue:
            x,y = queue.popleft()
            answer = max(answer, visited[y][x])
            for d in dirc:
                nx,ny = x+d[0], y+d[1]
                if 0<=nx<m and 0<=ny<n and visited[ny][nx]==0 and grid[ny][nx]==1:
                    queue.append([nx,ny])
                    visited[ny][nx] = visited[y][x]+1
                    grid[ny][nx] = 2
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1: return -1
        return answer