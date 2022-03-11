import sys
input = sys.stdin.readline
n = int(input())
arr = list(map(int, input().split()))
dp = [0]*n
summ = [0]*n
for i in range(n): summ[i] = arr[i]
for i in range(n):
    for j in range(i):
        if arr[j] < arr[i] and dp[j] > dp[i]:
            dp[i] = dp[j]
            summ[i] = max(summ[i], summ[j]+arr[i])
    dp[i] += 1
print(max(summ))