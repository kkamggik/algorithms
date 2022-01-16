import sys
sys.setrecursionlimit(100000)
def dfs(x,y,cnt):
    arr[y][x] = 1
    for d in dirc:
        nx,ny = x+d[0],y+d[1]
        if 0<=nx<m and 0<=ny<n and arr[ny][nx]==0:
            cnt = dfs(nx,ny,cnt+1)
    return cnt
dirc = [[1,0],[-1,0],[0,1],[0,-1]]
n,m,k = map(int, input().split())
arr = [[0]*m for _ in range(n)]
for _ in range(k):
    x1,y1,x2,y2 = map(int, input().split())
    for i in range(y1,y2):
        for j in range(x1,x2):
            arr[i][j] = 1
cnt = 0
answer = []
for i in range(n):
    for j in range(m):
        if arr[i][j] == 0:
            cnt += 1
            count = dfs(j,i,1)
            answer.append(count)
answer.sort()
print(cnt)
for a in answer:
    print(a,end=' ')