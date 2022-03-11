n,m = map(int, input().split())
arr = list(map(int, input().split()))
ans = 0
for i in range(n):
    for j in range(i+1,n):
        if arr[i]==arr[j]: continue
        else:
            ans += 1
print(ans)