import sys
import heapq
input = sys.stdin.readline
def dijkstra(v):
    dist = [2e9]*(n+1)
    dist[v] = 0
    heap = []
    heapq.heappush(heap, [0,v])
    while heap:
        d,v = heapq.heappop(heap)
        if dist[v] < d: continue
        for nxt,nd in arr[v]:
            cost = dist[v]+nd
            if cost < dist[nxt]:
                dist[nxt] = cost
                heapq.heappush(heap, [cost, nxt])
    return dist
n,m = map(int, input().split())
start = int(input())
arr = [[] for _ in range(n+1)]
for _ in range(m):
    a,b,c = map(int, input().split())
    arr[a].append([b,c])
dist = dijkstra(start)
for d in dist[1:]:
    if d == 2e9: print('INF')
    else: print(d)