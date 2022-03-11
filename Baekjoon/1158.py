n,k = map(int, input().split())
arr = [i for i in range(1,n+1)]
ans = '<'
num = 0
while arr:
    num += (k-1)
    if num >= len(arr):
        num = num%len(arr)
    ans += str(arr.pop(num))
    ans += ', '
ans = ans[:-2]+'>'
print(ans)
