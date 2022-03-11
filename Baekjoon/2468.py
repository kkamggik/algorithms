import sys
sys.setrecursionlimit(100000)
dirc = [[1,0],[-1,0],[0,1],[0,-1]]
def dfs(x,y,k):
    visited[y][x] = 1
    for d in dirc:
        nx = x+d[0]
        ny = y+d[1]
        if 0<=nx<n and 0<=ny<n and visited[ny][nx]==0 and arr[ny][nx]>k:
            dfs(nx,ny,k)
n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
answer = 0
for k in range(101):
    visited = [[0]*n for _ in range(n)]
    cnt = 0
    for i in range(n):
        for j in range(n):
            if arr[i][j] > k and visited[i][j]==0:
                cnt+=1
                dfs(j,i,k)
    answer = max(answer,cnt)
    if cnt == 0: break
print(answer)