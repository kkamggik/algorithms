import heapq
def dijkstra(start):
    dist = [1e9]*(n+1)
    dist[start] = 0
    heap = []
    heapq.heappush(heap,[0,start])
    while heap:
        d,idx = heapq.heappop(heap)
        if dist[idx] < d:
            continue
        for nidx, c in arr[idx]:
            cost = d + c
            if cost < dist[nidx]:
                dist[nidx] = cost
                heapq.heappush(heap, [cost, nidx])
    return dist

n,m,c = map(int, input().split())
arr = [[] for _ in range(n+1)]
for _ in range(m):
    x,y,z = map(int, input().split())
    arr[x].append([y,z])
dist = dijkstra(c)
count = 0
time = -1
for i in range(1,n+1):
    if i==c: continue
    if dist[i]==1e9: continue
    count += 1
    time = max(time, dist[i])
print(count, time)
