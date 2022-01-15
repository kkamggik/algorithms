mx = -1e9
mn = 1e9
def dfs(summ, idx):
    if sum(ops) == 0 or idx==len(nums):
        global mx,mn
        mx = max(mx, summ)
        mn = min(mn, summ)
        return
    if ops[0] > 0:
        ops[0] -= 1
        dfs(summ+nums[idx],idx+1)
        ops[0] += 1
    if ops[1] > 0:
        ops[1] -= 1
        dfs(summ-nums[idx],idx+1)
        ops[1] += 1
    if ops[2] > 0:
        ops[2] -= 1
        dfs(summ*nums[idx],idx+1)
        ops[2] += 1
    if ops[3] > 0:
        ops[3] -= 1
        if summ < 0:
            summ = -(abs(summ)//nums[idx])
            dfs(summ, idx+1)
        else:
            dfs(summ//nums[idx], idx+1)
        ops[3] += 1
n = int(input())
nums = list(map(int, input().split()))
# 덧셈 뺄셈 곱셈 나눗셈 순서
ops = list(map(int, input().split()))
dfs(nums[0],1)
print(mx)
print(mn)