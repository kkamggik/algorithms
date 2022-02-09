from collections import Counter
import sys
input = sys.stdin.readline
n = int(input())
arr = [int(input()) for _ in range(n)]
arr.sort()
nums = Counter(arr).most_common()
print(round(sum(arr)/n))
print(arr[n//2])
if len(nums)==1: print(nums[0][0])
else:
    if nums[0][0] == nums[1][0]: print(nums[1][0])
    else: print(nums[0][0])
print(arr[-1]-arr[0])
