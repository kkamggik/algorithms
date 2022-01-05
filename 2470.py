n = int(input())
arr = list(map(int, input().split()))
arr.sort()
left, right = 0, n-1
a,b,c = 0,0,2e9
while left < right:
    t = arr[right]+arr[left]
    if abs(t) < c:
        a,b = arr[left],arr[right]
        c = abs(t)
    if t < 0:
        left += 1
    else:
        right -= 1
print(a,b)