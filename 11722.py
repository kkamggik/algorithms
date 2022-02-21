import sys
input = sys.stdin.readline
n = int(input())
arr = list(map(int, input().split()))
arr.reverse()
dp = [0]*n
for i in range(n):
    for j in range(i):
        if dp[j] > dp[i] and arr[j] < arr[i]:
            dp[i] = dp[j]
    dp[i] += 1
print(max(dp))