answer = 0
dx = [1,-1,-1,1]
dy = [1,1,-1,-1]
def dfs(x, y, dirc, cnt):
    if (x==sx and y==sy and dirc == 3):
        global answer
        answer = max(answer, cnt-1)
    nx = x + dx[dirc]
    ny = y + dy[dirc]
    if(0<=nx<n and 0<=ny<n and desserts[arr[ny][nx]]==0):
        visited[ny][nx] = 1
        desserts[arr[ny][nx]] = 1
        dfs(nx, ny, dirc, cnt+1)
        desserts[arr[ny][nx]] = 0
        visited[ny][nx] = 0
    if(dirc+1 <= 3):
        nx = x + dx[dirc+1]
        ny = y + dy[dirc+1]
        if(0<=nx<n and 0<=ny<n and desserts[arr[ny][nx]]==0):
            visited[ny][nx] = 1
            desserts[arr[ny][nx]] = 1
            dfs(nx, ny, dirc+1, cnt+1)
            desserts[arr[ny][nx]] = 0
            visited[ny][nx] = 0
    
test = int(input())
desserts = [0]*(101)
for t in range(test):
    answer = 0
    n = int(input())
    visited = [[0]*n for _ in range(n)]
    arr = [list(map(int, input().split())) for _ in range(n)]
    for i in range(n-1):
        for j in range(n-1):
            sx = j
            sy = i
            dfs(j,i,0,1)
    if answer==0: answer = -1
    print("#{} {}".format(t+1, answer))
