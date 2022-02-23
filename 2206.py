import sys
from collections import deque
input = sys.stdin.readline
dirc = [[1,0],[-1,0],[0,1],[0,-1]]
def visit():
    queue = deque()
    queue.append([0,0,0])
    visited = [[[0]*2 for i in range(m)] for j in range(n)]
    visited[0][0][0] = 1
    while queue:
        x,y,flag = queue.popleft()
        if x==m-1 and y==n-1: return visited[y][x][flag]
        for d in dirc:
            nx,ny = x+d[0],y+d[1]
            if 0<=nx<m and 0<=ny<n and visited[ny][nx][flag]==0 and arr[ny][nx]=='0':
                visited[ny][nx][flag] = visited[y][x][flag]+1
                queue.append([nx,ny,flag])
            elif 0<=nx<m and 0<=ny<n and arr[ny][nx]=='1' and flag==0 and visited[ny][nx][1]==0:
                visited[ny][nx][1] = visited[y][x][flag]+1
                queue.append([nx,ny,1])
    return -1
n,m = map(int, input().split())
arr = [list(input()) for _ in range(n)]
answer = visit()
print(answer)