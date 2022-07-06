from collections import deque
T = int(input())
dirc = [[1,0],[-1,0],[0,1],[0,-1]]
for test_case in range(1, T + 1):
    n = int(input())
    arr = [list(input()) for _ in range(n)]
    visited = [[1e9]*n for _ in range(n)]
    visited[0][0] = 0
    queue = deque()
    queue.append([0,0])
    while queue:
        x,y = queue.popleft()
        for d in dirc:
            nx,ny = x+d[0], y+d[1]
            if 0<=nx<n and 0<=ny<n and visited[y][x]+int(arr[ny][nx]) < visited[ny][nx]:
                visited[ny][nx] = visited[y][x]+int(arr[ny][nx])
                queue.append([nx,ny])
    print("#{} {}".format(test_case, visited[n-1][n-1]))

