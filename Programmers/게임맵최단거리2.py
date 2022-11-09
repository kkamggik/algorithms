from collections import deque
def solution(maps):
    dx = [0,1,0,-1]
    dy = [1,0,-1,0]
    answer = 0
    queue = deque()
    queue.append([0,0])
    n,m = len(maps), len(maps[0])
    visited = [[0]*m for _ in range(n)]
    visited[0][0] = 1
    while queue:
        x, y  = queue.popleft()
        for d in range(4):
            tx = x + dx[d]
            ty = y + dy[d]
            if(0<=tx<m and 0<=ty<n and visited[ty][tx]==0 and maps[ty][tx]==1):
                visited[ty][tx] = visited[y][x] + 1
                queue.append([tx, ty])
    if(visited[n-1][m-1] == 0): return -1
    return visited[n-1][m-1] 