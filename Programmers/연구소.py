from itertools import combinations
from collections import deque
dx = [0,1,0,-1]
dy = [-1,0,1,0]
ans = 0
def bfs():
    visited = [[0]*m for _ in range(n)]
    queue = deque()
    for x, y in virus:
        queue.append([x, y])
        visited[y][x] = 1
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if(0<=nx<m and 0<=ny<n and visited[ny][nx]==0 and arr[ny][nx]==0):
                visited[ny][nx] = 1
                queue.append([nx, ny])
    cnt = 0
    global ans
    for i in range(n):
        for j in range(m):
            if(visited[i][j]==0 and arr[i][j]==0): cnt += 1
    ans = max(ans, cnt)


n,m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
walls = []
virus = []
for i in range(n):
    for j in range(m):
        if(arr[i][j] == 0): walls.append([j,i])
        elif(arr[i][j] == 2): virus.append([j,i])

for com in list(combinations(walls, 3)):
    arr[com[0][1]][com[0][0]] = 1
    arr[com[1][1]][com[1][0]] = 1
    arr[com[2][1]][com[2][0]] = 1
    bfs()
    arr[com[0][1]][com[0][0]] = 0
    arr[com[1][1]][com[1][0]] = 0
    arr[com[2][1]][com[2][0]] = 0
print(ans)
