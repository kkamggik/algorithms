T = int(input())
dirc = [[1,0],[0,1]]
def check(x,y,n,k,arr):
    cnt = 0
    for d in dirc:
        flag = True
        dx,dy = d[0],d[1]
        nx,ny = x+(-dx), y+(-dy)
        if (0<=nx<n and 0<=ny<n and arr[ny][nx]==0) or not(0<=nx<n and 0<=ny<n):
            t = 0
            c = 0
            while True:
                if 0<=x+(c*dx)<n and 0<=y+(c*dy)<n and arr[y+(c*dy)][x+(c*dx)]==1: t += 1
                else: break
                c += 1
            if t == k:
                cnt += 1
    return cnt
        
for test_case in range(1, T + 1):
    n,k = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(n)]
    rst = 0
    for i in range(n):
        for j in range(n):
            if arr[i][j] == 1:
                rst += check(j,i,n,k,arr)
    print(rst)