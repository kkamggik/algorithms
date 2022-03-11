import sys
input = sys.stdin.readline
def ispossible(target):
    group = 1
    total = 0
    for a in arr:
        total += a
        if total > target:
            group += 1
            total = a
    return group <= m
def solve(target):
    count = 0
    total = 0
    result = []
    group = m
    for i in range(n):
        total += arr[i]
        if total > target:
            group -= 1
            total = arr[i]
            result.append(count)
            count = 0
        count += 1
        if n-i == group: break
    while group:
        result.append(count)
        count = 1
        group -= 1
    return result

n,m = map(int, input().split())
arr = list(map(int, input().split()))
left = max(arr)
right = sum(arr)
while left <= right:
    mid = (left+right)//2
    if ispossible(mid):
        right = mid-1
    else:
        left = mid+1
print(left)
print(*solve(left))