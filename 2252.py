from collections import deque
import sys
input = sys.stdin.readline
n,m = map(int, input().split())
arr = [[] for _ in range(n+1)]
nodes = [0]*(n+1)
for _ in range(m):
    a,b = map(int, input().split())
    arr[a].append(b)
    nodes[b] += 1
queue = deque()
for i in range(1,n+1):
    if nodes[i]==0:
        queue.append(i)
while queue:
    x = queue.popleft()
    print(x,end=' ')
    for nxt in arr[x]:
        nodes[nxt] -= 1
        if nodes[nxt] == 0: queue.append(nxt)

