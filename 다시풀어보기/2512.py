n = int(input())
requests = list(map(int, input().split()))
m = int(input())
left, right = 0,max(requests)
while left <= right:
    mid = (left+right)//2
    bgt = 0
    for req in requests:
        if req > mid: bgt += mid
        else: bgt += req
    if bgt <= m:
        left = mid + 1
    else:
        right = mid - 1
print(right)
