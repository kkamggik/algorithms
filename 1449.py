import sys
input = sys.stdin.readline
n,m = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
idx = 0
cnt = 0
while idx < n:
    start = arr[idx]-0.5
    cnt += 1
    while idx < n and arr[idx] < start+m:
        idx += 1
print(cnt)