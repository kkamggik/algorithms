from copy import deepcopy
from collections import deque
dirc = [[1,0],[-1,0],[0,1],[0,-1]]
def virus():
    queue = deque()
    board = deepcopy(arr)
    for i in range(n):
        for j in range(m):
            if arr[i][j]==2: queue.append([j,i])
    while queue:
        x,y = queue.popleft()
        for d in dirc:
            nx,ny = x+d[0],y+d[1]
            if 0<=nx<m and 0<=ny<n and board[ny][nx]==0:
                board[ny][nx] = 2
                queue.append([nx,ny])
    cnt = 0
    for i in range(n):
        for j in range(m):
            if board[i][j]==0: cnt += 1
    global answer
    answer = max(answer, cnt)
def createWall(cnt):
    if cnt == 3:
        virus()
        return
    for i in range(n):
        for j in range(m):
            if arr[i][j] == 0:
                arr[i][j] = 1
                createWall(cnt+1)
                arr[i][j] = 0
answer = 0
n,m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
createWall(0)
print(answer)