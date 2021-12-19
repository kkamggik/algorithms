def binary(left, right):
    if left > right: return -1
    mid = (left+right)//2
    if arr[mid] == mid: return mid
    elif arr[mid] > mid:
        return binary(left, mid-1)
    else:
        return binary(mid+1, right)
n = int(input())
arr = list(map(int, input().split()))
arr.sort()
print(binary(0,n))