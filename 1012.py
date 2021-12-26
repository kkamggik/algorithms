from collections import deque
dirc = [[0,1],[0,-1],[1,0],[-1,0]]
def categorize(x,y):
    arr[y][x] = -1
    queue = deque()
    queue.append([x,y])
    while queue:
        x,y = queue.popleft()
        for d in dirc:
            nx,ny = x+d[0],y+d[1]
            if 0<=nx<m and 0<=ny<n and arr[ny][nx]==1:
                arr[ny][nx] = -1
                queue.append([nx,ny])
t = int(input())
for _ in range(t):
    cnt = 0
    m,n,k = map(int, input().split())
    arr = [[0]*m for i in range(n)]
    for i in range(k):
        x,y = map(int, input().split())
        arr[y][x] = 1
    for i in range(n):
        for j in range(m):
            if arr[i][j] == 1:
                categorize(j,i)
                cnt += 1
    print(cnt)
