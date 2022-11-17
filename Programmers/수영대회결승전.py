from collections import deque
test = int(input())
dx = [-1,0,1,0]
dy = [0,-1,0,1]
for t in range(test):
    answer = -1
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    sy, sx = map(int, input().split())
    fy, fx = map(int, input().split())
    queue = deque()
    queue.append([sx, sy])
    visited = [[0]*n for _ in range(n)]
    visited[sy][sx] = 1
    while queue:
        x, y = queue.popleft()
        if(x == fx and y == fy):
            break
        for i in range(4):
            tx = x + dx[i]
            ty = y + dy[i]
            if(0<=tx<n and 0<=ty<n and arr[ty][tx]!=1 and visited[ty][tx] == 0):
                if(arr[ty][tx] == 0):
                    visited[ty][tx] = visited[y][x] + 1
                else:
                    if((visited[y][x]-1) % 3 == 0):
                        visited[ty][tx] = visited[y][x] + 3
                    elif((visited[y][x]-1) % 3 == 1):
                        visited[ty][tx] = visited[y][x] + 2
                    else:
                        visited[ty][tx] = visited[y][x] + 1
                queue.append([tx, ty])
    if(visited[fy][fx]!=0): answer = visited[fy][fx]-1
    print(answer)
