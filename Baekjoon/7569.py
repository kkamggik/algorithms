from collections import deque
import sys
input = sys.stdin.readline
def check(tomato):
    for i in range(h):
        for j in range(n):
            for k in range(m):
                if tomato[i][j][k]==0: return False
    return True
dirc = [[1,0,0],[-1,0,0],[0,1,0],[0,-1,0],[0,0,1],[0,0,-1]]
m,n,h = map(int, input().split())
tomato = [[list(map(int, input().split())) for i in range(n)] for j in range(h)]
queue = deque()
for i in range(h):
    for j in range(n):
        for k in range(m):
            if tomato[i][j][k] == 1:
                queue.append([i,j,k,0])
answer = 0
while queue:
    z,y,x,cnt = queue.popleft()
    answer = max(answer, cnt)
    for d in dirc:
        nz,ny,nx = z+d[2], y+d[1], x+d[0]
        if 0<=nz<h and 0<=nx<m and 0<=ny<n and tomato[nz][ny][nx]==0:
            tomato[nz][ny][nx] = cnt+1
            queue.append([nz,ny,nx,cnt+1])
if check(tomato)==True: print(answer)
else: print(-1)