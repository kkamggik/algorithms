import sys
input = sys.stdin.readline
def solve(summ, idx, a, s, m, d):
    if idx == n:
        global mn,mx
        mn = min(mn, summ)
        mx = max(mx, summ)
        return
    if a > 0:
        solve(summ+nums[idx],idx+1, a-1, s, m, d)
    if s > 0:
        solve(summ-nums[idx],idx+1, a, s-1, m, d)
    if m > 0:
        solve(summ*nums[idx],idx+1, a, s, m-1, d)
    if d > 0:
        solve(int(summ/nums[idx]), idx+1, a, s, m, d-1)
n = int(input())
nums = list(map(int, input().split()))
a,b,c,d = map(int, input().split())
mx,mn = -1e9, 1e9
solve(nums[0],1,a,b,c,d)
print(mx)
print(mn)