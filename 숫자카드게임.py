n,m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
ans = -1
for i in range(n):
    ans = max(ans, min(arr[i]))
print(ans)