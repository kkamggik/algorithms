arr = []
maps = []
dx = [1,0,-1,0]
dy = [0,1,0,-1]
n, m = 0, 0
answer = []

def cycle(rx, ry, rd):
    stack = []
    stack.append([rx, ry, rd, 0])
    while stack:
        x, y, d, cnt = stack.pop()
        if(arr[y][x][d] == 1 and x==rx and y==ry and d==rd):
            global answer
            answer.append(cnt)
            return
        arr[y][x][d] = 1
        x = (x + dx[d]) % m
        y = (y + dy[d]) % n
        if(maps[y][x] == 'L'):
            if(d == 0): d = 3
            elif(d == 1): d = 0
            elif(d == 2): d = 2
            else: d = 1
        elif(maps[y][x] == 'R'):
            d = (d+1) % 4
        stack.append([x, y, d, cnt+1])
            
def solution(grid):
    global arr, n ,m, maps
    maps = grid[:]
    n,m = len(grid), len(grid[0])
    arr = [[[0]*(4) for i in range(m)] for j in range(n)]
    for i in range(n):
        for j in range(m):
            for k in range(4):
                if(arr[i][j][k] == 0):
                    cycle(j, i, k)
    return answer

print(solution(["SL","LR"]))