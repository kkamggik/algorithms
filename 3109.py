import sys
input = sys.stdin.readline
from collections import deque
dirc = [[1,-1],[1,0],[1,1]]
def dfs(x,y):
    global visited
    if x==m-1:
        visited[y][x] = 1
        return True
    for d in dirc:
        nx, ny = x+d[0], y+d[1]
        if 0<=nx<m and 0<=ny<n and visited[ny][nx] == 0 and arr[ny][nx]=='.':
            visited[ny][nx] = 1
            if dfs(nx,ny) == True: return True
    return False
    
n,m = map(int, input().split())
arr = [list(input().strip()) for _ in range(n)] 
visited = [[0]*m for _ in range(n)]
answer = 0
for i in range(n):
    if visited[i][0]==0:
        visited[i][0] = 1
        if dfs(0,i) == True: answer += 1
print(answer)