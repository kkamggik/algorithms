class Solution(object):
    def shortestPath(self, grid, k):
        """
        :type grid: List[List[int]]
        :type k: int
        :rtype: int
        """
        dirc = [[1,0],[-1,0],[0,1],[0,-1]]
        n,m = len(grid),len(grid[0])
        visited = set()
        visited.add((0,0,k))
        queue = deque()
        queue.append([0,0,k,0])
        res = 1e9
        while queue:
            x,y,z,c = queue.popleft()
            if x==m-1 and y==n-1:
                return c
            for d in dirc:
                nx,ny = x+d[0],y+d[1]
                if 0<=nx<m and 0<=ny<n:
                    if grid[ny][nx]==0 and (nx,ny,z) not in visited:
                        visited.add((nx,ny,z))
                        queue.append([nx,ny,z,c+1])
                    elif z>0 and (nx,ny,z-1) not in visited:
                        visited.add((nx,ny,z-1))
                        queue.append([nx,ny,z-1,c+1])
        return -1
        