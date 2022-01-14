def factorial(n):
    rst = 1
    for i in range(1,n+1):
        rst *= i
    return rst
t = int(input())
for _ in range(t):
    n,m = map(int, input().split())
    ans = factorial(m) // (factorial(n)*factorial(m-n))
    print(ans)