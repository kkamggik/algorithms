n,m = map(int, input().split())
arr = [int(input()) for _ in range(n)]
arr.sort()
left, right = arr[0], arr[-1]
ans = 1e9
while left <= right:
    cnt = 1
    mid = (right + left)//2
    prev = arr[0]
    close = 1e9
    for i in range(1, n):
        if arr[i] > prev + mid:
            cnt += 1
            close = min(close, arr[i]-prev)
            prev = arr[i]
    if cnt == m:
        ans = min(ans, close)
    if cnt >= m:
        left = mid + 1
    elif cnt < m:
        right = mid - 1
print(ans)