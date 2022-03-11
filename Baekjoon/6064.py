def find(m,n,x,y):
    while x <= m*n:
        if (x-y)%n == 0: return x
        x += m
    return -1
tests = int(input())
for _ in range(tests):
    m,n,x,y = map(int, input().split())
    print(find(m,n,x,y))
