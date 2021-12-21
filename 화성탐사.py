import heapq
dirc = [[1,0],[-1,0],[0,1],[0,-1]]
n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
dist = [[1e9]*n for _ in range(n)]
x,y = 0,0
heap = []
heapq.heappush(heap, [arr[y][x],x,y])
dist[y][x] = arr[y][x]
while heap:
    dst, x, y = heapq.heappop(heap)
    if dist[y][x] < dst: continue
    for d in dirc:
        nx = x+d[0]
        ny = y+d[1]
        if 0<=nx<n and 0<=ny<n:
            cost = dst + arr[ny][nx]
            if cost < dist[ny][nx]:
                dist[ny][nx] = cost
                heapq.heappush(heap, [cost, nx, ny])
print(dist[n-1][n-1])