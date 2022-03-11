import heapq
def dijkstra(start):
    dist = [1e9]*(n+1)
    dist[1] = 0
    heap = []
    heapq.heappush(heap, [0, start])
    while heap:
        d,x = heapq.heappop(heap)
        if dist[x] < d: continue
        for nx, nc in arr[x]:
            cost = d + nc
            if cost < dist[nx]:
                dist[nx] = cost
                heapq.heappush(heap, [cost, nx])
    return dist

n,m = map(int, input().split())
arr = [[] for _ in range(n+1)]
for _ in range(m):
    a,b = map(int, input().split())
    arr[a].append([b,1])
    arr[b].append([a,1])
dist = dijkstra(1)
ans = 0
for i in range(1,n+1):
    ans = max(ans, dist[i])
print(dist.index(ans), ans, dist.count(ans))