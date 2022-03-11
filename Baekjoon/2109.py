import heapq
import sys
input = sys.stdin.readline
n = int(input())
heap = []
for _ in range(n):
    p,d = map(int, input().split())
    heapq.heappush(heap, [-d,p])
answer = 0
last = 0
if heap: last = -heap[0][0]
works = []
for i in range(last,0,-1):
    while heap and -heap[0][0] >= i:
        d,p = heapq.heappop(heap)
        heapq.heappush(works, [-p,-d])
    if works:
        p,d = heapq.heappop(works)
        answer += -p
print(answer)