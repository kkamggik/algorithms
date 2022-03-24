class Solution(object):
    def highestRankedKItems(self, grid, pricing, start, k):
        """
        :type grid: List[List[int]]
        :type pricing: List[int]
        :type start: List[int]
        :type k: int
        :rtype: List[List[int]]
        """
        dirc = [[0,1],[0,-1],[1,0],[-1,0]]
        queue = deque()
        n,m = len(grid), len(grid[0])
        visited = [[-1]*m for _ in range(n)]
        sy,sx = start
        visited[sy][sx] = 0
        low, high = pricing
        queue.append([sx,sy])
        answer = []
        while queue:
            x,y = queue.popleft()
            if low<=grid[y][x]<=high:
                answer.append([x,y,visited[y][x],grid[y][x]])
            for d in dirc:
                nx,ny = x+d[0], y+d[1]
                if 0<=nx<m and 0<=ny<n and visited[ny][nx]==-1 and grid[ny][nx]!=0:
                    visited[ny][nx] = visited[y][x]+1
                    queue.append([nx,ny])
        answer.sort(key = lambda x:(x[2], x[3], x[1], x[0]))
        rst = []
        for i in range(k):
            if i+1 > len(answer):
                break
            else:
                x,y,d,p = answer[i]
                rst.append([y,x])
        return rst