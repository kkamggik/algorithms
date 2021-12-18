dirc = [[0,-1],[1,0],[0,1],[-1,0]]
n,m = map(int, input().split())
x,y,d = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
ans = 1
turn = 0
while True:
    d = (d-1)%4
    nx,ny = x+dirc[d][0], y+dirc[d][1]
    if 0<=ny<n and 0<=nx<m and arr[ny][nx]==0:
        arr[ny][nx] = -1
        x,y = nx,ny
        turn = 0
        ans += 1
    else:
        turn += 1
    if turn == 4:
        back = (d-2)%4
        nx,ny = x+dirc[back][0], y+dirc[back][1]
        if arr[ny][nx] != 0: break
        else:
            x,y = nx,ny
print(ans)