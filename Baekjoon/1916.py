import sys
import heapq
input = sys.stdin.readline
def dijkstra(v,dest):
    dist = [1e9]*(n+1)
    dist[v] = 0
    heap = []
    heapq.heappush(heap, [v,0])
    while heap:
        v,d = heapq.heappop(heap)
        if dist[v] < d: continue
        for nxt, cost in arr[v]:
            mcost = d+cost
            if mcost < dist[nxt]:
                dist[nxt] = mcost
                heapq.heappush(heap, [nxt,mcost])
    return dist[dest]
n = int(input())
m = int(input())
arr = [[] for _ in range(n+1)]
for _ in range(m):
    a,b,c = map(int, input().split())
    arr[a].append([b,c])
s,e = map(int, input().split())
dist = dijkstra(s,e)
print(dist)