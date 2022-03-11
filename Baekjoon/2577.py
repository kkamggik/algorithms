a = int(input())
b = int(input())
c = int(input())
nums = [0]*10
for i in str(a*b*c):
    nums[int(i)] += 1
for n in nums:
    print(n)