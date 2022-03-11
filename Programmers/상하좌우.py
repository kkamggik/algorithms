dirc = {'U': (0,-1), 'D': (0,1), 'L': (-1,0), 'R': (1,0)}
n = int(input())
s = list(input().split())
x,y = 1,1
for d in s:
    nx, ny = x+dirc[d][0], y+dirc[d][1]
    if 0<nx<=n and 0<ny<=n:
        x,y = nx,ny
print(y,x)
