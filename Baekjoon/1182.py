import sys
input = sys.stdin.readline
n,m = map(int, input().split())
arr = list(map(int, input().split()))
cnt = 0
def subset(idx, summ):
    if idx >= n: return
    summ += arr[idx]
    if summ == m:
        global cnt
        cnt += 1
    subset(idx+1, summ)
    subset(idx+1, summ-arr[idx])
subset(0,0)
print(cnt)