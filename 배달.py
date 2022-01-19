import heapq
def dijkstra(N,arr):
    dist = [1e9]*N
    dist[1] = 0
    heap = []
    heapq.heappush(heap, [0,1])
    while heap:
        d,x = heapq.heappop(heap)
        if dist[x] < d: continue
        for nd,nx in arr[x]:
            ndist = dist[x] + nd
            if ndist < dist[nx]:
                dist[nx] = ndist
                heapq.heappush(heap, [ndist,nx])
    return dist
def solution(N, road, K):
    answer = N
    arr = [[] for _ in range(N+1)]
    for a,b,c in road:
        arr[a].append([c,b])
        arr[b].append([c,a])
    dist = dijkstra(N+1,arr)
    for d in dist[1:]:
        if d > K: answer -= 1
    return answer