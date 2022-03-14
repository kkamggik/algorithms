class Solution(object):
    def bfs(self,x,y,grid):
        dirc = [[1,0],[-1,0],[0,1],[0,-1]]
        n,m = len(grid), len(grid[0])
        queue = deque()
        queue.append([x,y])
        global visited
        visited[y][x] = 1
        cnt = 0
        while queue:
            x,y = queue.popleft()
            cnt += 1
            for d in dirc:
                nx,ny = x+d[0],y+d[1]
                if 0<=nx<m and 0<=ny<n and visited[ny][nx]==0 and grid[ny][nx]==1:
                    visited[ny][nx] = 1
                    queue.append([nx,ny])
        return cnt
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        n,m = len(grid), len(grid[0])
        global visited
        visited = [[0]*m for _ in range(n)]
        answer = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1 and visited[i][j]==0:
                    answer = max(answer,self.bfs(j,i,grid))
        return answer