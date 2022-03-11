from collections import deque
dirc = [[1,0],[-1,0],[0,1],[0,-1]]
n,m = map(int, input().split())
arr = [list(input()) for _ in range(n)]
queue = deque()
queue.append([0,0])
visit = [[-1]*m for _ in range(n)]
visit[0][0] = 1
while queue:
    x,y = queue.popleft()
    for d in dirc:
        nx,ny = x+d[0],y+d[1]
        if 0<=nx<m and 0<=ny<n and visit[ny][nx]==-1 and arr[ny][nx]=='1':
            visit[ny][nx] = visit[y][x]+1
            queue.append([nx,ny])
print(visit[n-1][m-1])