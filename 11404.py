n = int(input())
m = int(input())
arr = [[1e9]*(n+1) for _ in range(n+1)]
for _ in range(m):
    a,b,c = map(int, input().split())
    arr[a][b] = min(arr[a][b], c)
for k in range(1,n+1):
    arr[k][k] = 0
    for i in range(1,n+1):
        for j in range(1,n+1):
            arr[i][j] = min(arr[i][j], arr[i][k]+arr[k][j])
for i in range(1,n+1):
    for j in range(1,n+1):
        print(arr[i][j],end=" ")
    print()
