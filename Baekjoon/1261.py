import sys
from collections import deque
input = sys.stdin.readline
dirc = [[0,-1],[0,1],[1,0],[-1,0]]
m,n = map(int, input().split())
arr = [list(input().strip()) for _ in range(n)]
queue = deque()
queue.append([0,0])
visited = [[2e9]*m for _ in range(n)]
visited[0][0] = 0
while queue:
    x,y = queue.popleft()
    for d in dirc:
        nx,ny = x+d[0],y+d[1]
        if 0<=nx<m and 0<=ny<n:
            if arr[ny][nx]=='0' and visited[ny][nx] > visited[y][x]:
                visited[ny][nx] = visited[y][x]
                queue.append([nx,ny])
            if arr[ny][nx]=='1' and visited[ny][nx] > visited[y][x]+1:
                visited[ny][nx] = visited[y][x]+1
                queue.append([nx,ny])
print(visited[n-1][m-1])