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
        global positive, negative, zero
        if arr[y][x]==-1: negative += 1
        elif arr[y][x]==0: zero += 1
        else: positive += 1
        return
    mid = m//3
    dfs(x,y,mid)
    dfs(x+mid,y,mid)
    dfs(x+2*mid,y,mid)
    dfs(x,y+mid,mid)
    dfs(x+mid,y+mid,mid)
    dfs(x+2*mid,y+mid,mid)
    dfs(x,y+2*mid,mid)
    dfs(x+mid,y+2*mid,mid)
    dfs(x+2*mid,y+2*mid,mid)
n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
visited = [[0]*n for _ in range(n)]
negative = 0
positive = 0
zero = 0
dfs(0,0,n)
print(negative)
print(zero)
print(positive)

# def clip_paper(x, y, n):
#     global neg, neut, pos
#     num_check = paper[x][y]
#     for i in range(x, x + n):
#         for j in range(y, y + n):
#             if(paper[i][j] != num_check):
#                 for k in range(3):
#                     for l in range(3):
#                         clip_paper(x + k * n//3, y + l * n//3, n//3)
#                 return
