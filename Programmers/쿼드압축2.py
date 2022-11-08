maps = []
one, zero = 0, 0
def check(x, y, d):
    t = maps[y][x]
    for i in range(y, y+d):
        for j in range(x, x+d):
            if(maps[i][j]!=t): return 0
    return 1
def quad(x, y, d):
    if(check(x, y, d)==1):
        global one, zero
        if(maps[y][x]==1): one += 1
        else: zero += 1
        return
    else:
        n = d//2
        quad(x, y, n)
        quad(x+n, y, n)
        quad(x, y+n, n)
        quad(x+n, y+n, n)
def solution(arr):
    global maps
    maps = arr[:]
    quad(0, 0, len(arr))
    return [zero, one]