answer = []
visited = []
dirc = [[1,0],[-1,0],[0,1],[0,-1]]
grid = []
n,m = 0,0
def cycle(x,y,d):
    stack = []
    stack.append([x,y,d,0])
    while stack:
        nx,ny,nd,cnt = stack.pop()
        if nx==x and ny==y and nd==d and visited[ny][nx][nd]==1:
            answer.append(cnt)
            return
        visited[ny][nx][nd] = 1
        nx,ny = nx+dirc[nd][0],ny+dirc[nd][1]
        nx,ny = nx%m,ny%n
        if grid[ny][nx] == 'L':
            if nd == 0: nd = 3
            elif nd == 1: nd = 2
            elif nd == 2: nd = 0
            else: nd = 1
        elif grid[ny][nx] == 'R':
            if nd == 0: nd = 2
            elif nd == 1: nd = 3
            elif nd == 2: nd = 1
            else: nd = 0
        stack.append([nx,ny,nd,cnt+1])
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
                    cycle(j,i,k)
    answer.sort()
    return answer