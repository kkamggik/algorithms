n,m = map(int, input().split())
arr = [[1e9]*n for _ in range(n)]
for i in range(n):
    arr[i][i] = 0
for _ in range(m):
    a,b = map(int, input().split())
    arr[a-1][b-1] = 1
    arr[b-1][a-1] = 1
x,y = map(int, input().split())
for k in range(n):
    for i in range(n):
        for j in range(n):
            arr[i][j] = min(arr[i][j], arr[i][k]+arr[k][j])
if arr[0][y-1]==1e9 or arr[y-1][x-1]==1e9:
    print(-1)
else:
    print(arr[0][y-1]+arr[y-1][x-1])
