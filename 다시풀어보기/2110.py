n,m = map(int, input().split())
arr = [int(input()) for _ in range(n)]
arr.sort()
left, right = 1, arr[-1]-arr[0]
while left <= right:
    mid = (left+right)//2
    cnt = 1
    prev = arr[0]
    for d in arr[1:]:
        if d-prev >= mid:
            cnt += 1
            prev = d
    if cnt >= m:
        left = mid+1
    else:
        right = mid-1
print(right)