import heapq
n = int(input())
fuels = []
for _ in range(n):
    a,b = map(int, input().split())
    heapq.heappush(fuels, [a,b])
l,p = map(int, input().split())
answer = 0
heap = []
while  p < l:
    while fuels and fuels[0][0] <= p:
        a,b = heapq.heappop(fuels)
        heapq.heappush(heap, [-b, a])
    if not heap:
        answer = -1
        break
    b,a = heapq.heappop(heap)
    p += -b
    answer += 1
print(answer)