import sys
input = sys.stdin.readline
n,m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
new = [[0]*m for _ in range(n)]
for i in range(n):
    high = 0
    for j in range(m):
        if arr[i][j] > high:
            high = arr[i][j]
            x,y = j,i
    new[y][x] = high
for i in range(m):
    high = 0
    for j in range(n):
        if arr[j][i] > high:
            high = arr[j][i]
            x,y = i,j
    new[y][x] = high
answer = 0
for i in range(n):
    for j in range(m):
        if new[i][j] == 0:
            answer += arr[i][j]
print(answer)