left, right = 0, n-1
# lower bound
while left < right:
    mid = (left+right)//2
    if target <= arr[mid]:
        right = mid
    else:
        left = mid + 1
    return left

# upper bound
while left < right:
    mid = (left+right)//2
    if target < arr[mid]:
        right = mid
    else:
        left = mid + 1
    return left
