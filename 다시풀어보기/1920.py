import sys
input = sys.stdin.readline
def search(left,right,target):
    while left <= right:
        mid = (left+right)//2
        if nums[mid]==target: return 1
        elif nums[mid] < target:
            left = mid + 1
        else: 
            right = mid - 1
    return 0
n = int(input())
nums = list(map(int, input().split()))
nums.sort()
m = int(input())
arr = list(map(int, input().split()))
for num in arr:
    print(search(0,n-1,num))