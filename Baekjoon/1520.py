import sys
sys.setrecursionlimit(1000000)
input = sys.stdin.readline
dirc = [[0,1],[0,-1],[1,0],[-1,0]]
def dfs(x,y):
    if x==m-1 and y==n-1: return 1
    if visited[y][x]!=-1:
        return visited[y][x]
    visited[y][x] = 0
    for d in dirc:
        nx,ny = x+d[0],y+d[1]
        if 0<=nx<m and 0<=ny<n and arr[ny][nx]<arr[y][x]:
            visited[y][x] += dfs(nx,ny)
    return visited[y][x]
n,m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
visited = [[-1]*m for _ in range(n)]
print(dfs(0,0))