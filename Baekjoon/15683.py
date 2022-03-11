from copy import deepcopy
from collections import deque
import sys
input = sys.stdin.readline
dirc = [[-1,0],[0,-1],[1,0],[0,1]]
def draw(narr, visit):
    cnt = 0
    queue = deque()
    for i in range(len(visit)):
        x,y,t = cctv[i]
        d = visit[i]
        queue.append([x,y,d])
        if t==1:
            while queue:
                x,y,d = queue.popleft()
                narr[y][x] = '#'
                nx,ny = x+dirc[d][0],y+dirc[d][1]
                if 0<=nx<m and 0<=ny<n and narr[ny][nx]!=6:
                    queue.append([nx,ny,d])
        elif t==2:
            queue.append([x,y,d+2])
            while queue:
                x,y,d = queue.popleft()
                narr[y][x] = '#'
                nx,ny = x+dirc[d][0],y+dirc[d][1]
                if 0<=nx<m and 0<=ny<n and narr[ny][nx]!=6:
                    queue.append([nx,ny,d])
        elif t==3:
            queue.append([x,y,(d+1)%4])
            while queue:
                x,y,d = queue.popleft()
                narr[y][x] = '#'
                nx,ny = x+dirc[d][0],y+dirc[d][1]
                if 0<=nx<m and 0<=ny<n and narr[ny][nx]!=6:
                    queue.append([nx,ny,d])
        elif t==4:
            queue.append([x,y,(d+1)%4])
            queue.append([x,y,(d+2)%4])
            while queue:
                x,y,d = queue.popleft()
                narr[y][x] = '#'
                nx,ny = x+dirc[d][0],y+dirc[d][1]
                if 0<=nx<m and 0<=ny<n and narr[ny][nx]!=6:
                    queue.append([nx,ny,d])
        elif t==5:
            queue.append([x,y,1])
            queue.append([x,y,2])
            queue.append([x,y,3])
            while queue:
                x,y,d = queue.popleft()
                narr[y][x] = '#'
                nx,ny = x+dirc[d][0],y+dirc[d][1]
                if 0<=nx<m and 0<=ny<n and narr[ny][nx]!=6:
                    queue.append([nx,ny,d])
    for i in range(n):
        for j in range(m):
            if narr[i][j]==0: cnt+=1
    global answer
    answer = min(answer, cnt)
def dfs(cnt, visit):
    if cnt == len(visit):
        narr = deepcopy(arr)
        draw(narr, visit)
        return
    x,y,d = cctv[cnt]
    if d in [1,3,4]:
        for j in range(4):
            visit[cnt] = j
            dfs(cnt+1, visit)
            visit[cnt] = -1
    elif d == 2:
        for j in range(2):
            visit[cnt] = j
            dfs(cnt+1, visit)
            visit[cnt] = -1
    else:
        visit[cnt] = 0
        dfs(cnt+1, visit)
        visit[cnt] = -1
n,m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
cctv = []
answer = 1e9
for i in range(n):
    for j in range(m):
        if 0<arr[i][j]<6:
            cctv.append([j,i, arr[i][j]])
visit = [-1]*len(cctv)
dfs(0, visit)
print(answer)
