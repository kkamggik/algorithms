import heapq
import sys
input = sys.stdin.readline
n,k = map(int, input().split())
answer = 0
heap = []
for _ in range(n):
    m,v = map(int, input().split())
    heapq.heappush(heap, [m,v])
bags = []
for _ in range(k):
    heapq.heappush(bags, int(input()))
possible = []
while bags:
    b = heapq.heappop(bags)
    while heap and heap[0][0] <= b:
        m,v = heapq.heappop(heap)
        heapq.heappush(possible, -v)
    if possible:
        v = -heapq.heappop(possible)
        answer += v
print(answer)