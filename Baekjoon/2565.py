import sys
input = sys.stdin.readline
n = int(input())
lines = [0]*(501)
for _ in range(n):
    a,b = map(int, input().split())
    lines[a] = b
dp = [0]*(501)
for i in range(1,501):
    if lines[i]==0: continue
    for j in range(1,i):
        if lines[j] < lines[i] and dp[j] > dp[i]:
            dp[i] = dp[j]
    dp[i] += 1
print(n-max(dp))
