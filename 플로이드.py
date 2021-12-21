n = int(input())
arr = [[1e9]*n for _ in range(n)]
m = int(input())
for _ in range(m):
    a,b,c = map(int, input().split())
    arr[a-1][b-1] = min(c, arr[a-1][b-1])
for i in range(n):
    arr[i][i] = 0
for k in range(n):
    for i in range(n):
        for j in range(n):
            arr[i][j] = min(arr[i][j], arr[i][k]+arr[k][j])
print(arr)