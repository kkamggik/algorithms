import sys
input = sys.stdin.readline
def exist(x,y,t):
    if(t in arr[y]):
        return False
    for a in range(9):
        if(t == arr[a][x]):
            return False
    nx,ny = 3*(x//3),3*(y//3)
    for a in range(ny,ny+3):
        for b in range(nx,nx+3):
            if(arr[a][b]==t):
                return False
    return True
def dfs(idx):
    if idx == len(empty):
        for row in arr: print(*row)
        sys.exit()
    x,y = empty[idx]
    for i in range(1,10):
        if exist(x,y,i) == True:
            arr[y][x] = i
            dfs(idx+1)
            arr[y][x] = 0
arr = [list(map(int, input().split())) for _ in range(9)]
empty = []
for i in range(9):
    for j in range(9):
        if arr[i][j] == 0:
            empty.append([j,i])
dfs(0)