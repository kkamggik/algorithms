import sys
input = sys.stdin.readline
n,m = map(int, input().split())
cost = [int(input()) for _ in range(n)]
coins = 0
for i in range(1,n):
    if cost[i] > cost[i-1]:
        coin = m//cost[i-1]
        m -= coin*cost[i-1]
        coins += coin
    else:
        if coins > 0:
            m += coins*cost[i-1]
            coins = 0
if coins > 0:
    m += coins*cost[-1]
print(m)