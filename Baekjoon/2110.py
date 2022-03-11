import sys
input = sys.stdin.readline
n,c = map(int, input().split())
houses = [int(input()) for _ in range(n)]
houses.sort()
left, right = 1, houses[-1]-houses[0]
while left <= right:
    mid = (left+right)//2
    prev = houses[0]
    cnt = 1
    for i in range(1,n):
        if houses[i]-prev >= mid:
            prev = houses[i]
            cnt += 1
    if cnt >= c:
        left = mid+1
    else:
        right = mid-1
print(right)