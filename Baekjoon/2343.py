n,m = map(int, input().split())
arr = list(map(int, input().split()))
left,right = max(arr),sum(arr)
while left<=right:
    mid = (left+right)//2
    cnt = 1
    curr = arr[0]
    for a in arr[1:]:
        if a+curr <= mid:
            curr += a
        else:
            curr = a
            cnt += 1
    if cnt > m:
        left = mid+1
    else:
        right = mid-1
print(left)