import sys
input = sys.stdin.readline
dirc = [[0,-1],[1,0],[0,1],[-1,0]]
n,m = map(int, input().split())
y,x,d = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
cnt = 0
while True:
    if arr[y][x] == 0:
        arr[y][x] = -1
        cnt += 1
    flag = False
    for i in range(1,5):
        nd = (d-i)%4
        nx,ny = x+dirc[nd][0], y+dirc[nd][1]
        if 0<=nx<m and 0<=ny<n and arr[ny][nx]==0:
            flag = True
            break
    if flag==True:
        x,y,d = nx,ny,nd
    else:
        nx,ny = x-dirc[d][0],y-dirc[d][1]
        if 0<=nx<m and 0<=ny<n and arr[ny][nx]!=1:
            x,y,d = nx,ny,d
        else: break
print(cnt)
    

