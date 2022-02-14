from collections import deque
import sys
input = sys.stdin.readline
dirc = [[0,1],[0,-1],[1,0],[-1,0]]
n,m = map(int, input().split())
arr = [list(input().strip()) for _ in range(n)]
water = deque()
queue = deque()
visit = [[-1]*m for _ in range(n)]
for i in range(n):
    for j in range(m):
        if arr[i][j] == 'D': dest = [j,i]
        elif arr[i][j] == 'S': 
            post = [j,i]
            arr[i][j] = '.'
            queue.append([j,i,0])
        elif arr[i][j] == '*': 
            water.append([j,i])
            visit[i][j] = 0
while water:
    x,y = water.popleft()
    for d in dirc:
        nx,ny = x+d[0],y+d[1]
        if 0<=nx<m and 0<=ny<n and visit[ny][nx]==-1 and arr[ny][nx]=='.':
            visit[ny][nx] = visit[y][x]+1
            water.append([nx,ny])
answer = -1
visit[dest[1]][dest[0]] = 1e9
while queue:
    x,y,cnt = queue.popleft()
    if x==dest[0] and y==dest[1]:
        answer = cnt
        break
    for d in dirc:
        nx,ny = x+d[0],y+d[1]
        if 0<=nx<m and 0<=ny<n and (visit[ny][nx]==-1 or visit[ny][nx]>(cnt+1)) and arr[ny][nx]!='X':
            visit[ny][nx] = -2
            queue.append([nx,ny,cnt+1])
if answer == -1: print('KAKTUS')
else: print(answer)