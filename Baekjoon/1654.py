n,k = map(int, input().split())
lines = [int(input()) for _ in range(n)]
left,right = 1, max(lines)
while left <= right:
    mid = (left+right)//2
    cnt = 0
    for line in lines:
        cnt += (line//mid)
        if cnt >= k: break
    if cnt < k: right = mid-1
    else: left = mid+1
print(right)