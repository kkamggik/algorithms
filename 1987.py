import sys
input = sys.stdin.readline
dirc = [[1,0],[-1,0],[0,1],[0,-1]]
def dfs(x,y,cnt):
    global answer
    answer = max(answer,cnt)
    for d in dirc:
        nx,ny = x+d[0],y+d[1]
        if 0<=nx<m and 0<=ny<n and alp[ord(arr[ny][nx])-65]==0:
            alp[ord(arr[ny][nx])-65] = 1
            dfs(nx,ny,cnt+1)
            alp[ord(arr[ny][nx])-65] = 0
answer = 0
n,m = map(int, input().split())
arr = [list(input()) for _ in range(n)]
alp = [0]*26
alp[ord(arr[0][0])-65] = 1
dfs(0,0,1)
print(answer)