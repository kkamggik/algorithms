import heapq
import sys
input = sys.stdin.readline
def dijkstra(v,arr):
    dist = [1e9]*(n+1)
    dist[v] = 0
    heap = []
    heapq.heappush(heap,[v,0])
    while heap:
        v,d = heapq.heappop(heap)
        if dist[v] < d: continue
        for nxt, cost in arr[v]:
            mcost = cost + d
            if mcost < dist[nxt]:
                dist[nxt] = mcost
                heapq.heappush(heap, [nxt, mcost])
    return dist
n,m,x = map(int, input().split())
arr = [[] for _ in range(n+1)]
rarr = [[] for _ in range(n+1)]
for _ in range(m):
    a,b,c = map(int, input().split())
    arr[a].append([b,c])
    rarr[b].append([a,c])
dist = dijkstra(x,arr)
rdist = dijkstra(x,rarr)
answer = 0
for v in range(1,n+1):
    answer = max(answer, dist[v]+rdist[v])
print(answer)