import heapq
import sys
input = sys.stdin.readline
n,m = map(int, input().split())
heap = []
indegree = [0]*(n+1)
out = [[] for _ in range(n+1)]
for _ in range(m):
    a,b = map(int, input().split())
    indegree[b] += 1
    out[a].append(b)
for i in range(1,n+1):
    if indegree[i] == 0:
        heapq.heappush(heap,i)
while heap:
    x = heapq.heappop(heap)
    print(x,end=' ')
    for p in out[x]:
        indegree[p] -= 1
        if indegree[p] == 0: heapq.heappush(heap, p)
    