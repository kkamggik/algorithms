from collections import deque
dirc = [[1,0],[-1,0],[0,-1],[0,1]]
for test_case in range(10):
    test = int(input())
    n = 16
    arr = [list(input()) for _ in range(n)]
    visited = [[0]*n for _ in range(n)]
    sx = sy = fx = fy  = -1
    for i in range(n):
        for j in range(n):
            if arr[i][j]=='2':
                sx,sy = j,i
            if arr[i][j]=='3':
                fx,fy = j,i
    visited[sy][sx] = 1
    queue = deque()
    queue.append([sx,sy])
    res = 0
    while queue:
        x,y = queue.popleft()
        if x==fx and y==fy:
            res = 1
            break
        for d in dirc:
            nx,ny = x+d[0],y+d[1]
            if 0<=nx<n and 0<=ny<n and visited[ny][nx]==0 and arr[ny][nx]!='1':
                visited[ny][nx] = 1
                queue.append([nx,ny])
    print("#{} {}".format(test, res))

