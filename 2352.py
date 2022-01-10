import sys
input = sys.stdin.readline
def search(a):
    left,right = 0,len(rst)-1
    while left <= right:
        mid = (left+right)//2
        if rst[mid] < a:
            left = mid+1
        else:
            right = mid-1
    return left
n = int(input())
arr = list(map(int, input().split()))
rst = []
for a in arr:
    if not rst or rst[-1]<a:
        rst.append(a)
    else:
        rst[search(a)] = a
print(rst)