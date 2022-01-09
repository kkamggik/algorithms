n = int(input())
arr = list(map(int, input().split()))
arr.sort()
left, right = 0, n-1
answer = 1e9
a,b = 0,0
while left < right:
    t = arr[left]+arr[right]
    if abs(t) < answer:
        a,b = arr[left],arr[right]
        answer = abs(t)
    if t < 0:
        left += 1
    else:
        right -= 1
print(a,b)