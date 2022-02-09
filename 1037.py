def gcd(a,b):
    while b > 0:
        a,b = b,a%b
    return a
def lcm(a,b):
    return a*b // gcd(a,b)
n = int(input())
arr = list(map(int, input().split()))
ans = lcm(1,arr[0])
for i in range(1,n):
    ans = lcm(ans, arr[i])
if ans != max(arr): print(ans)
else: print(max(arr)*min(arr))