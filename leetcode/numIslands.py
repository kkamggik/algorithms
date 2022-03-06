from collections import deque
class Solution(object):
    def bfs(self,x,y,n,m,grid):
        queue = deque()
        queue.append([x,y])
        global visited, dirc
        visited[y][x] = 1
        while queue:
            x,y = queue.popleft()
            for d in dirc:
                nx,ny = x+d[0],y+d[1]
                if 0<=nx<m and 0<=ny<n and visited[ny][nx]==0 and grid[ny][nx]=="1":
                    visited[ny][nx] = 1
                    queue.append([nx,ny])
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        global visited, dirc
        m,n = len(grid[0]),len(grid)
        visited = [[0]*m for _ in range(n)]
        dirc = [[1,0],[-1,0],[0,1],[0,-1]]
        cnt = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j]=="1" and visited[i][j] == 0:
                    self.bfs(j,i,n,m,grid)
                    cnt += 1
        return cnt
        
        