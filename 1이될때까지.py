n,k = map(int, input().split())
ans = 0
while n!=1:
    if n%k == 0:
        n /= k
        ans += 1
    else:
        n -= 1
        ans += 1
print(ans)
