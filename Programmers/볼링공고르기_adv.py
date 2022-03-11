n,m = map(int, input().split())
arr = list(map(int, input().split()))
balls = [0]*11
for i in arr:
    balls[i] += 1
ans = 0
for i in range(1,m+1):
    n -= balls[i]
    ans += (balls[i] * n)
print(ans)