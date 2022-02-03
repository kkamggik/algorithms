import heapq
import sys
input = sys.stdin.readline
n,k = map(int, input().split())
heap = []
for _ in range(n):
    m,v = map(int, input().split())
    heapq.heappush(heap, [m,v])
bags = [int(input()) for _ in range(k)]
bags.sort()
jems = []
answer = 0
for bag in bags:
    while heap and heap[0][0] <= bag:
        m,v = heapq.heappop(heap)
        heapq.heappush(jems, [-v,m])
    if jems:
        v,m = heapq.heappop(jems)
        answer += -v
print(answer)