import sys
sys.setrecursionlimit(100000)
dirc = [[0,1],[0,-1],[1,0],[-1,0],[-1,-1],[1,1],[-1,1],[1,-1]]
def dfs(x,y,idx):
    visited[y][x] = idx
    for d in dirc:
        nx = x+d[0]
        ny = y+d[1]
        if 0<=nx<m and 0<=ny<n and visited[ny][nx]==0 and arr[ny][nx]==1:
            dfs(nx,ny,idx)
while True:
    m,n = map(int, input().split())
    if m==0 and n==0: break
    arr = [list(map(int, input().split())) for _ in range(n)]
    visited = [[0]*m for _ in range(n)]
    cnt = 0
    for i in range(n):
        for j in range(m):
            if arr[i][j] == 1 and visited[i][j]==0:
                cnt += 1
                dfs(j,i,cnt)
    print(cnt)