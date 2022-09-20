def factorial(n):
    fact = 1
    for i in range(1,n+1):
        fact *= i
    return fact
t = int(input())
for i in range(t):
    n,m = map(int, input().split())
    # m이 n보다 크고 최대 연결할 수 있는 다리의 갯수는 n이다.
    # m개의 지역에 n개의 다리를 놓을 수 있는 경우의 수를 구하는 것이기 떄문에
    # mCn 으로 표현할 수 있다. = m! / (m-n)!n!
    rst = factorial(m) // (factorial(m-n)*factorial(n))
    print(rst)