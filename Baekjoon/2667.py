from collections import deque
dirc = [[0,1],[0,-1],[1,0],[-1,0]]
def name(x,y,addr):
    cnt = 1
    visit[y][x] = addr
    queue = deque()
    queue.append([x,y])
    while queue:
        x,y = queue.popleft()
        for d in dirc:
            nx,ny = x+d[0],y+d[1]
            if 0<=nx<n and 0<=ny<n and visit[ny][nx]==0 and arr[ny][nx]=='1':
                visit[ny][nx] = addr
                queue.append([nx,ny])
                cnt += 1
    return cnt
n = int(input())
arr = [list(map(str,input())) for _ in range(n)]
visit = [[0]*n for _ in range(n)]
addr = 1
ans = []
for i in range(n):
    for j in range(n):
        if arr[i][j] == '1' and visit[i][j]==0:
            cnt = name(j,i,addr)
            ans.append(cnt)
            addr += 1
print(addr-1)
ans.sort()
for i in ans: print(i)