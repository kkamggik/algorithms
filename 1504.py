import heapq
import sys
input = sys.stdin.readline
def dijkstra(v):
    dist = [2e9]*(n+1)
    dist[v] = 0
    heap = []
    heapq.heappush(heap,[v,0])
    while heap:
        v,d = heapq.heappop(heap)
        if d < dist[v]: continue
        for nxt,cost in arr[v]:
            tcost = d + cost
            if tcost < dist[nxt]:
                dist[nxt] = tcost
                heapq.heappush(heap,[nxt, tcost])
    return dist
n,m = map(int, input().split())
arr = [[] for _ in range(n+1)]
for _ in range(m):
    a,b,c = map(int, input().split())
    arr[a].append([b,c])
    arr[b].append([a,c])
a,b = map(int, input().split())
a1 = dijkstra(1)
a2 = dijkstra(a)
a3 = dijkstra(b)
answer = min(a1[a]+a2[b]+a3[n], a1[b]+a3[a]+a2[n])
if answer < 2e9: print(answer)
else: print(-1)