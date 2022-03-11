import sys
input = sys.stdin.readline
n = int(input())
dist = list(map(int, input().split()))
cost = list(map(int, input().split()))
d = sum(dist)
mcost = cost[0]
answer = d*mcost
for i in range(n-1):
    if cost[i] < mcost:
        answer -= (mcost-cost[i])*d
        mcost = cost[i]
    d -= dist[i]
print(answer)