# 이 문제 재귀 안쓰고 풀어야된다네;;.. 다시 풀어봐야댐...

answer = []
visited = []
dirc = [[1,0],[-1,0],[0,1],[0,-1]]
grid = []
n,m = 0,0
sx,sy,sd = 0,0,0
def dfs(x,y,d,cnt):
    x,y = x%m, y%n
    #나아갈 방향...
    if grid[y][x] == 'L':
        if d == 0: d = 3
        elif d == 1: d = 2
        elif d == 2: d = 0
        else: d = 1
    elif grid[y][x] == 'R':
        if d == 0: d = 2
        elif d == 1: d = 3
        elif d == 2: d = 1
        else: d = 0
    nx,ny = x+dirc[d][0],y+dirc[d][1]
    nx,ny = nx%m,ny%n
    if x==sx and y==sy and d==sd and visited[sy][sx][sd] == 1:
        answer.append(cnt)
        return
    visited[y][x][d] = 1
    dfs(nx,ny,d,cnt+1)
def solution(tgrid):
    global n,m,visited,grid,sx,sy,sd
    grid = tgrid[:]
    n = len(grid)
    m = len(grid[0])
    visited = [[[0]*4 for i in range(m)] for j in range(n)]
    for i in range(n):
        for j in range(m):
            for k in range(4):
                if visited[i][j][k] == 0:
                    sx,sy,sd = j,i,k
                    visited[i][j][k] = 1
                    nx,ny = j+dirc[k][0],i+dirc[k][1]
                    dfs(nx,ny,k,1)
    answer.sort()
    return answer
print(solution(	["R", "R"]))