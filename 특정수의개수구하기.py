from bisect import bisect_left, bisect_right
n,m = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
left = bisect_left(arr, m)
right = bisect_right(arr, m)
if left==n:
    print(-1)
else:
    print(right-left)