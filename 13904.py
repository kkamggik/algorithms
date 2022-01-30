import heapq
n = int(input())
heap = []
for _ in range(n):
    d,w = map(int, input().split())
    heapq.heappush(heap, [-d,w])
answer = 0
last = -heap[0][0]
works = []
for i in range(last,0,-1):
    while heap and -heap[0][0] >= i:
        d,w = heapq.heappop(heap)
        heapq.heappush(works, [-w,-d])
    if works:
        w,d = heapq.heappop(works)
        answer += -w
print(answer)