n = int(input())
arr = list(map(int, input().split()))
budget = int(input())
left,right = 0,max(arr)
ans = 0
while left <= right:
    mid = (left+right)//2
    curr = 0
    for i in arr:
        if i > mid:
            curr += mid
        else:
            curr += i
    if curr <= budget:
        ans = max(ans, mid)
    if curr < budget:
        left = mid+1
    else:
        right = mid-1
print(ans)