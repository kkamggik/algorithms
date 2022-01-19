from collections import deque
from copy import deepcopy
dirc = [[1,0],[0,-1],[-1,0],[0,1]]
def bfs(x,y):
    queue = deque()
    queue.append([x,y])
    temp[y][x] = 0
    while queue:
        x,y = queue.popleft()
        for d in dirc:
            nx,ny = x+d[0],y+d[1]
            if 0<=nx<m and 0<=ny<n and temp[ny][nx]>0:
                temp[ny][nx] = 0
                queue.append([nx,ny])   
def melting(x,y):
    cnt = 0
    for d in dirc:
        nx,ny = x+d[0],y+d[1]
        if 0<=nx<m and 0<=ny<n and arr[ny][nx]==0:
            cnt += 1
    return cnt
def count_land():
    for i in range(n):
        for j in range(m):
            if arr[i][j] > 0: return True
    return False
n,m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
answer = 0
while True:
    if count_land()==False:
        answer = 0
        break
    answer += 1
    temp = [[0]*m for _ in range(n)]
    for i in range(1,n-1):
        for j in range(1,m-1):
            if arr[i][j] > 0:
                cnt = melting(j,i)
                temp[i][j] = arr[i][j] - cnt
                if temp[i][j] < 0: temp[i][j] = 0
    arr = deepcopy(temp)
    land = 0
    for i in range(1,n-1):
        for j in range(1,m-1):
            if temp[i][j] > 0:
                bfs(j,i)
                land += 1
    if land >= 2: break
print(answer)
