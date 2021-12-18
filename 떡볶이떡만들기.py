n,m = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
left, right = 0, arr[-1]
ans = mid
while left <= right:
    mid = (left+right)//2
    rem = 0
    for i in arr:
        if i > mid: rem += (i-mid)
    if rem < m:
        right = mid - 1
    else:
        left = mid + 1
        ans = mid
print(mid)