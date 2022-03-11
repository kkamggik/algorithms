import sys
input = sys.stdin.readline
n = int(input())
arr = list(map(int, input().split()))
dp = [0]*n
for i in range(n):
    for j in range(i):
        if arr[i] > arr[j]:
            dp[i] = max(dp[j], dp[i])
    dp[i] += 1
dp2 = [0]*n
arr = arr[::-1]
for i in range(n):
    for j in range(i):
        if arr[i] > arr[j]:
            dp2[i] = max(dp2[j], dp2[i])
    dp2[i] += 1
dp2 = dp2[::-1]
answer = 0
for i in range(n):
    answer = max(answer, dp[i]+dp2[i]-1)
print(answer)