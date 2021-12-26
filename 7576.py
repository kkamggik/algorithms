from collections import deque
dirc = [[0,1],[0,-1],[1,0],[-1,0]]
def check():
    cnt = 0
    for i in range(n):
        for j in range(m):
            if arr[i][j] == 0:
                return -1
            cnt = max(cnt, arr[i][j])
    return cnt-1
m,n = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
queue = deque()
for i in range(n):
    for j in range(m):
        if arr[i][j] == 1:
            queue.append([j,i])
if len(queue) == n*m:
    print(0)
else:
    while queue:
        x,y = queue.popleft()
        for d in dirc:
            nx,ny = x+d[0],y+d[1]
            if 0<=nx<m and 0<=ny<n and arr[ny][nx]==0:
                arr[ny][nx] = arr[y][x]+1
                queue.append([nx,ny])
print(check())