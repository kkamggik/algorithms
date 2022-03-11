import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
dirc = [[1,0],[0,-1],[-1,0],[0,1]]
def dfs(x,y):
    if dp[y][x]: return dp[y][x]
    dp[y][x] = 1
    for d in dirc:
        nx,ny = x+d[0],y+d[1]
        if 0<=nx<n and 0<=ny<n:
            if arr[y][x] < arr[ny][nx]:
                dp[y][x] = max(dp[y][x], dfs(nx,ny)+1)
    return dp[y][x]
n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
dp = [[0]*n for _ in range(n)]
answer = 0
for i in range(n):
    for j in range(n):
        answer = max(answer, dfs(j,i))
print(answer)
