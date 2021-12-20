n = int(input())
time = []
cost = []
for _ in range(n):
    t,c = map(int, input().split())
    time.append(t)
    cost.append(c)
dp = [0]*(n+1)
ans = 0
for i in range(n-1,-1,-1):
    t = time[i] + i
    if t <= n:
        dp[i] = max(dp[t]+cost[i], ans)
        ans = dp[i]
    else:
        dp[i] = ans
print(ans)