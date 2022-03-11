from collections import deque
dirc = [[1,0],[-1,0],[0,1],[0,-1]]
def freeze(x,y):
    queue = deque()
    queue.append([x,y])
    arr[y][x] = '1'
    while queue:
        x,y = queue.popleft()
        for d in dirc:
            nx,ny = x+d[0],y+d[1]
            if 0<=nx<m and 0<=ny<n and arr[ny][nx]=='0':
                arr[ny][nx] = '1'
                queue.append([nx,ny])

n,m = map(int, input().split())
arr = [list(input()) for _ in range(n)]
ans = 0
for i in range(n):
    for j in range(m):
        if arr[i][j] == '0':
            freeze(j,i)
            ans += 1
print(ans)