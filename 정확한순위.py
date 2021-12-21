n,m = map(int, input().split())
arr = [[1e9]*(n+1) for _ in range(n+1)]
for i in range(1,n+1):
    arr[i][i] = 0
for _ in range(m):
    a,b = map(int, input().split())
    arr[a][b] = 1
for k in range(1,n+1):
    for i in range(1,n+1):
        for j in range(1,n+1):
            arr[i][j] = min(arr[i][j], arr[i][k]+arr[k][j])
ans = 0
for i in range(1,n+1):
    cnt = 0
    for j in range(1,n+1):
        if arr[i][j]!=1e9 or arr[j][i]!=1e9:
            cnt += 1
    if cnt == n:
        ans += 1
print(ans)