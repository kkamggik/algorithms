import sys
input = sys.stdin.readline
n,m = map(int, input().split())
arr = [[1e9]*(n+1) for _ in range(n+1)]
for _ in range(m):
    a,b = map(int, input().split())
    arr[a][b] = 1
    arr[b][a] = 1
for k in range(1,n+1):
    arr[k][k] = 0
    for i in range(1,n+1):
        for j in range(1,n+1):
            arr[i][j] = min(arr[i][j], arr[i][k]+arr[k][j])
ans = [1e9]*(n+1)
for i in range(1,n+1):
    ans[i] = sum(arr[i][1:])
m = min(ans)
print(ans.index(m))