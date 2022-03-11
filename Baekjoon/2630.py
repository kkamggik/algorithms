import sys
input = sys.stdin.readline
def check(x,y,mid):
    compare = arr[y][x]
    for i in range(y,y+mid):
        for j in range(x,x+mid):
            if compare!=arr[i][j]: return False
    return True

def dfs(x,y,m):
    if check(x,y,m) == True:
        global white, blue
        if arr[y][x]==1: blue += 1
        else: white += 1
        return
    mid = m//2
    dfs(x,y,mid)
    dfs(x+mid,y,mid)
    dfs(x,y+mid,mid)
    dfs(x+mid,y+mid,mid)
n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
visited = [[0]*n for _ in range(n)]
white = 0
blue = 0
dfs(0,0,n)
print(white)
print(blue)