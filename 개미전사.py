n = int(input())
arr = list(map(int, input().split()))
dp = [0]*(n+1)
dp[1] = arr[0]
dp[2] = max(arr[0],arr[1])
for i in range(3,n+1):
    dp[i] = max(dp[i-2]+arr[i-1],dp[i-1])
print(dp[n])
