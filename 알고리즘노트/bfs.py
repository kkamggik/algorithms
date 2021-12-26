from collections import deque
dirc = [[0,1],[0,-1],[1,0],[-1,0]]
def bfs(x,y):
    arr[y][x] = -1
    queue = deque()
    queue.append([x,y])
    while queue:
        x,y = queue.popleft()
        for d in dirc:
            nx,ny = x+d[0],y+d[1]
            if 0<=nx<m and 0<=ny<n and arr[ny][nx]==1:
                arr[ny][nx] = -1
                queue.append([nx,ny])