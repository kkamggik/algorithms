import sys
sys.setrecursionlimit(100000)
dirc = [[1,0],[-1,0],[0,1],[0,-1]]
def notColorBlind(x,y,color):
    visited[y][x] = 1
    for d in dirc:
        nx,ny = x+d[0],y+d[1]
        if 0<=nx<n and 0<=ny<n and visited[ny][nx]==0 and arr[ny][nx]==color:
            notColorBlind(nx,ny,color)
def colorBlind(x,y,color):
    visited[y][x] = 1
    for d in dirc:
        nx,ny = x+d[0],y+d[1]
        if 0<=nx<n and 0<=ny<n and visited[ny][nx]==0:
            if (color=="R" or color=="G") and (arr[ny][nx]=="R" or arr[ny][nx]=="G"):
                colorBlind(nx,ny,color)
            elif color==arr[ny][nx]:
                colorBlind(nx,ny,color)
            
n = int(input())
arr = [list(input()) for _ in range(n)]
visited = [[0]*n for _ in range(n)]
cnt1,cnt2 = 0,0
for i in range(n):
    for j in range(n):
        if visited[i][j]==0:
            cnt1 += 1
            notColorBlind(j,i,arr[i][j])
visited = [[0]*n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if visited[i][j]==0:
            cnt2 += 1
            colorBlind(j,i,arr[i][j])
print(cnt1, cnt2)