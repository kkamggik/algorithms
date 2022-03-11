num = list(input())
nums = [0]*9
for n in num:
    x = int(n)
    if x==9: x=6
    nums[x] += 1
nums[6] = nums[6]//2 + nums[6]%2
print(max(nums))
