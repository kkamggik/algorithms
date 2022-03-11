def binary(start, end, target):
    if start > end:
        return -1
    mid = (start+end)//2
    if arr[mid] > target:
        return binary(start, mid-1, target)
    elif arr[mid] < target:
        return binary(mid+1, end, target)
    else:
        return mid
n = int(input())
arr = list(map(int, input().split()))
m = int(input())
search = list(map(int, input().split()))
arr.sort()
for i in search:
    if binary(0,n,i) != -1:
        print('yes',end=' ')
    else:
        print('no',end=' ')